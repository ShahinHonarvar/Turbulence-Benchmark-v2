def submatrix_with_particular_sum(matrix):
    """
    Given a two-dimensional numpy matrix of integers, return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -25.
    """
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    if matrix[k][l] - matrix[i][j] == -25:
                        result.append((i, j, k, l))
    if len(result) == 0:
        return []
    return result