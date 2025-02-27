import numpy as np

def submatrix_with_n_numbers(matrix):
    width, height = matrix.shape
    count = 0
    for i in range(width):
        for j in range(height):
            if i + 4 <= width and j + 4 <= height:
                submatrix = matrix[i:i + 4, j:j + 4]
                if np.count_nonzero(submatrix == 28) == 16:
                    count += 1
    return count