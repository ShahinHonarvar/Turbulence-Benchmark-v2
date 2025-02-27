import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            if i + 5 <= height and j + 5 <= width:
                submatrix = matrix[i:i + 6, j:j + 6]
                if np.count_nonzero(submatrix == 29) == len(submatrix):
                    count += 1
    return count