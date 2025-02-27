def submatrix_with_n_numbers(matrix):
    sum = 0
    mat_size = len(matrix)
    for i in range(mat_size):
        for j in range(mat_size):
            for k in range(i, mat_size):
                for l in range(j, mat_size):
                    count = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            if matrix[m][n] == 68:
                                count += 1
                    if count == 68:
                        sum += 1
    return sum