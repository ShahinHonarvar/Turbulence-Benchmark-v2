def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    if matrix[k][l] - matrix[i][j] == 175 and (k - i > 0 and l - j > 0):
                        count += 1
    return count