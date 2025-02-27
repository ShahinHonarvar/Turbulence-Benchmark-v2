from itertools import combinations

def submatrix_with_particular_sum(matrix):
    diagonal_sums = {}
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] != 0:
                diagonal_sums[i, j] = matrix[i][j]
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    sum_of_submatrix = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            sum_of_submatrix += diagonal_sums.get((m, n), 0)
                    if sum_of_submatrix == 16:
                        return [(i, j), (k, l)]
    return []