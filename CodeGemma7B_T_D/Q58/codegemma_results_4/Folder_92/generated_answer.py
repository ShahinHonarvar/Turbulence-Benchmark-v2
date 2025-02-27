import numpy as np

def submatrix_with_n_numbers(matrix, n=8):
    """Returns the count of all submatrices of the given matrix that contain n integers each."""
    count = 0
    for y1 in range(matrix.shape[0]):
        for y2 in range(y1, matrix.shape[0]):
            for x1 in range(matrix.shape[1]):
                for x2 in range(x1, matrix.shape[1]):
                    submatrix = matrix[y1:y2 + 1, x1:x2 + 1]
                    if submatrix.size == n:
                        count += 1
    return count