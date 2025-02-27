import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    width, height = matrix.shape
    for y1 in range(height):
        for y2 in range(y1, height):
            for x1 in range(width):
                for x2 in range(x1, width):
                    submatrix = matrix[y1:y2 + 1, x1:x2 + 1]
                    if submatrix.size == 56 and submatrix.sum() == 2800:
                        count += 1
    return count