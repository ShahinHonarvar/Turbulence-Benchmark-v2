import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Takes one argument which is a two-dimensional numpy matrix of integers.
    Returns the count of all submatrices of the given matrix that contain 78 integers each.
    """
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(i + 1, matrix.shape[0]):
            for k in range(matrix.shape[1]):
                for l in range(k + 1, matrix.shape[1]):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if np.count_nonzero(submatrix == 78) == 78:
                        count += 1
    return count