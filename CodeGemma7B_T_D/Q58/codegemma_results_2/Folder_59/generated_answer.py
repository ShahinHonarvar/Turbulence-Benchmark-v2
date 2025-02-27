import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Counts the number of submatrices of a given matrix that contain [N] numbers each.

    Args:
        matrix: A 2D numpy matrix of integers.

    Returns:
        The count of submatrices with [N] numbers or 0 if no such submatrices exist.
    """
    submatrix_count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == 76:
                        submatrix_count += 1
    return submatrix_count