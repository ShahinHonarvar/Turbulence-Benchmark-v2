import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            if matrix[row, col] == 1:
                count += 1
                for r in range(row + 1, rows):
                    if matrix[r, col] == 1:
                        count += 1
                for c in range(col + 1, cols):
                    if matrix[row, c] == 1:
                        count += 1
                for r in range(row + 1, rows):
                    for c in range(col + 1, cols):
                        if matrix[r, c] == 1:
                            count += 1
    return count