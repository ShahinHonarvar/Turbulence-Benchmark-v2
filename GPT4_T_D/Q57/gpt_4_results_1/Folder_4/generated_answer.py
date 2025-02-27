import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for x in range(rows):
        for y in range(cols):
            for width in range(1, cols - y + 1):
                for height in range(1, rows - x + 1):
                    submatrix = matrix[x:x + height, y:y + width]
                    if submatrix.sum() == 87:
                        result.append(submatrix)
    return result