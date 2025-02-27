import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    This function takes a two-dimensional numpy matrix of integers and returns
    the number of submatrices containing exactly 130 integers each. If no such
    submatrix is found, it returns 0.

    Note: This function assumes that the 'matrix' has more than one row and column.
    """
    height, width = matrix.shape
    count = 0
    if height > 1 and width > 1:
        for i in range(height - 1):
            for j in range(width - 1):
                num = matrix[i, j] + matrix[i, j + 1] + matrix[i + 1, j] + matrix[i + 1, j + 1]
                if num == 130:
                    count += 1
    return count