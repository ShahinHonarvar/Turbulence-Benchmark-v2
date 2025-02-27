def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    if matrix[i][j:l + 1].shape[0] * matrix[i][j:l + 1].shape[1] == 186:
                        count += 1
    return count