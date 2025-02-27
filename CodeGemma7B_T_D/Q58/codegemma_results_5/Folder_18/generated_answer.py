import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Write a function called 'submatrix_with_n_numbers' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the count of all submatrices of the given matrix that contain 104 integers each. If no such submatrix is found, the function should return 0.
    """
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.count_nonzero(submatrix) == 104:
                        count += 1
    return count