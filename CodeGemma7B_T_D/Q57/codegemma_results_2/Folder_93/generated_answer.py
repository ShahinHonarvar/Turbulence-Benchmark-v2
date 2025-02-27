def submatrix_with_particular_sum(matrix):
    """
    Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -65. If no such submatrix is found, the function should return an empty list.
    """
    return [submatrix for submatrix in [[matrix[r:r + i][c:c + j] for j in range(i + 1)] for r in range(len(matrix) - i + 1) for i in range(len(matrix) - r + 1)] if sum((sum(row) for row in submatrix)) == -65]