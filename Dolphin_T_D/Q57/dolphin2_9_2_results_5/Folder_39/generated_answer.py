import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    size_x, size_y = matrix.shape
    for x in range(size_x):
        for y in range(size_y):
            for size in range(min(size_x - x, size_y - y) + 1):
                if sum(matrix[x:x + size, y:y + size]) == 66:
                    submatrix = matrix[x:x + size, y:y + size]
                    submatrices.append(submatrix)
    return submatrices