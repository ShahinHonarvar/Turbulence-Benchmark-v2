def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k + 1, len(matrix[0])):
                    if len({matrix[i][k], matrix[i][l], matrix[j][k], matrix[j][l]}) == 2:
                        count += 1
    return count