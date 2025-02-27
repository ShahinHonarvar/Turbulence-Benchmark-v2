import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for y in range(height):
        for x in range(width):
            if matrix[y, x] == 1:
                for h in range(height - y):
                    for w in range(width - x):
                        submatrix = matrix[y:y + h + 1, x:x + w + 1]
                        if submatrix.size == 176:
                            count += 1
    return count