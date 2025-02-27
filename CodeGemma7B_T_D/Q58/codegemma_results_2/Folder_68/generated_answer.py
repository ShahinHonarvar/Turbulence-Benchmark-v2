def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(len(matrix[i])):
                for l in range(k + 1, len(matrix[j])):
                    if matrix[i][k] + matrix[j][l] == 74:
                        count += 1
    return count