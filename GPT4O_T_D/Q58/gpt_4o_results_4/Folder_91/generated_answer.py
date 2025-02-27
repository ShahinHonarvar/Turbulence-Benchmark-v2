import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    if rows < 1 or cols < 5:
        return 0
    for i in range(rows):
        for j in range(cols - 4):
            submatrix = matrix[i, j:j + 5]
            if submatrix.size == 5:
                count += 1
    for i in range(cols):
        for j in range(rows - 4):
            submatrix = matrix[j:j + 5, i]
            if submatrix.size == 5:
                count += 1
    if rows >= 5 and cols >= 5:
        for i in range(rows - 4):
            for j in range(cols - 4):
                submatrix = matrix[i:i + 5, j:j + 5].flatten()
                if submatrix.size == 5:
                    count += 2
    return count