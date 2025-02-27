def submatrix_with_particular_sum(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i + 1, len(matrix) + 1):
                for l in range(j + 1, len(matrix) + 1):
                    submatrix = matrix[i:k][j:l]
                    if sum(sum(submatrix, [])) == 394:
                        return [[i, j], [k - 1, l - 1]]
    return []