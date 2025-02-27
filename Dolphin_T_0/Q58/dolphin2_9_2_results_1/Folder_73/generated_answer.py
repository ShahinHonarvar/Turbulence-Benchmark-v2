import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            if matrix[i, j] == 1:
                for x in range(i, height):
                    for y in range(j, width):
                        submatrix = matrix[i:x + 1, j:y + 1]
                        if submatrix.size == 41:
                            submatrix_count += 1
    return submatrix_count