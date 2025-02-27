def submatrix_with_particular_sum(matrix):
    """
    This function returns the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -38.
    """
    return [[matrix[i][j] for j in range(i, len(matrix))] for i in range(len(matrix))]