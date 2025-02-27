def submatrix_with_particular_sum(matrix):
    """
    Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers.
    The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 35.
    If no such submatrix is found, the function should return an empty list.
    """
    x = 0
    l = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(len(matrix)):
                for h in range(k + 1, len(matrix)):
                    for m in range(len(matrix[0])):
                        for n in range(m + 1, len(matrix[0])):
                            summ = matrix[i][k][m] + matrix[i][k][n] - matrix[i][j][m] - matrix[i][j][n] + matrix[j][h][m] + matrix[j][h][n] - matrix[h][m][n] - matrix[h][k][n]
                            if summ == 35:
                                l.append((matrix[i][k][m], matrix[i][k][n], matrix[i][j][m], matrix[i][j][n], matrix[j][h][m], matrix[j][h][n], matrix[h][m][n], matrix[h][k][n]))
    if len(l) == 0:
        return []
    else:
        return l