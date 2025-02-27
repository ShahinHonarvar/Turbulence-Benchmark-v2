def submatrix_with_n_numbers(matrix):
    """
    Count the number of submatrices with n consecutive elements.
    """
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 76:
                for k in range(i, len(matrix)):
                    for l in range(j, len(matrix[0])):
                        if matrix[k][l] == 76:
                            count += 1
    return count