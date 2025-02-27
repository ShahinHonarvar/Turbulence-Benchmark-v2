import numpy as np

def submatrix_with_n_numbers(matrix):
    """This function counts the number of submatrices of a given matrix that contain 88 integers each."""
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Error: Input to submatrix_with_n_numbers must be a numpy matrix')
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[k])):
                    if np.array_equal(matrix[i:k + 1, j:l + 1], np.ones((k + 1 - i, l + 1 - j)) * 88):
                        count += 1
    return count