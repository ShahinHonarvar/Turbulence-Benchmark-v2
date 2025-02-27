import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    A function that takes one argument which is a two-dimensional numpy matrix of integers. 
    The function returns the count of all submatrices of the given matrix that contain 159 integers each. 
    If no such submatrix is found, the function returns 0.
    """
    submatrices = []
    h, w = matrix.shape
    for i in range(h):
        for j in range(w):
            for k in range(i + 1, h + 1):
                for l in range(j + 1, w + 1):
                    if len(matrix[i:k, j:l].ravel()) == 159:
                        submatrices.append(matrix[i:k, j:l])
    return len(submatrices)