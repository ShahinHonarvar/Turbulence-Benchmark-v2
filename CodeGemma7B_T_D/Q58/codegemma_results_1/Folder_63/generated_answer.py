from numpy import array

def submatrix_with_n_numbers(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if 57 in [matrix[i][j] for i in range(k + 1 - i) for j in range(l + 1 - j)]:
                        count += 1
    return count