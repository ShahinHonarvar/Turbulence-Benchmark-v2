def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k, len(matrix[0])):
                    if matrix[i][j] % 53 == 0 and matrix[k][l] % 53 == 0 and ((j - i + 1) * (l - k + 1) == 53):
                        count += 1
    return count