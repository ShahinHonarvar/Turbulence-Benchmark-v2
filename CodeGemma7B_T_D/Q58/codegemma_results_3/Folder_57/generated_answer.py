def submatrix_with_n_numbers(matrix):
    """
            Write a function called 'submatrix_with_n_numbers' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the count of all submatrices of the given matrix that contain 92 integers each. If no such submatrix is found, the function should return 0.
            """
    n = matrix.shape[0]
    m = matrix.shape[1]
    count = 0
    for i in range(n - 8):
        for j in range(m - 8):
            if (matrix[i][j] == 0 and matrix[i + 1][j] == 1 and (matrix[i + 2][j] == 0) and (matrix[i + 3][j] == 0) and (matrix[i + 4][j] == 0) and (matrix[i + 5][j] == 0) and (matrix[i + 6][j] == 0) and (matrix[i + 7][j] == 1)).all():
                for k in range(i + 1, n):
                    for l in range(j + 1, m):
                        if (matrix[i][j] == matrix[k][l] and matrix[i + 1][j] == matrix[k][l + 1] and (matrix[i + 2][j] == matrix[k][l + 2]) and (matrix[i + 3][j] == matrix[k][l + 3]) and (matrix[i + 4][j] == matrix[k][l + 4]) and (matrix[i + 5][j] == matrix[k][l + 5]) and (matrix[i + 6][j] == matrix[k][l + 6]) and (matrix[i + 7][j] == matrix[k][l + 7]) or (matrix[i + 1][j] == matrix[k][l] and matrix[i][j + 1] == matrix[k][l + 1] and (matrix[i + 2][j] == matrix[k][l + 2]) and (matrix[i + 3][j] == matrix[k][l + 3]) and (matrix[i + 4][j] == matrix[k][l + 4]) and (matrix[i + 5][j] == matrix[k][l + 5]) and (matrix[i + 6][j] == matrix[k][l + 6]) and (matrix[i + 7][j] == matrix[k][l + 7]))).all():
                            count += 1
    return count