import numpy as np

def submatrix_with_n_numbers(matrix):
    length, width = matrix.shape
    counter = 0
    for i in range(length - 8):
        for j in range(width - 8):
            if (matrix[i:i + 9, j:j + 9] == 97).all():
                counter += 1
    return counter