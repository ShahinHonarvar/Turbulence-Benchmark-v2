import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 111
    width = len(matrix[0])
    height = len(matrix)
    count = 0
    for i in range(height):
        for j in range(width):
            if i + n <= height and j + n <= width:
                submatrix = np.array(matrix[i:i + n, j:j + n])
                if np.all(submatrix == n):
                    count += 1
    return count