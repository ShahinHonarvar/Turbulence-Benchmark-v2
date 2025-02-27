import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for i in range(row + 1, rows + 1):
                for j in range(col + 1, cols + 1):
                    submatrix = matrix[row:i, col:j]
                    if submatrix.size == 17:
                        count += 1
    return count