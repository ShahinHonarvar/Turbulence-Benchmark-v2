import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Input: 2-D numpy array of integers.

    Output: count of submatrices that contain n numbers.
    """
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            submatrix = matrix[i:i + 20, j:j + 20]
            if submatrix.shape[0] == 20 and submatrix.shape[1] == 20 and (submatrix.size == 400):
                count += 1
    return count