import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    if rows < 4 or cols < 4:
        return 0
    count = 0
    for i in range(rows - 3):
        for j in range(cols - 3):
            count += 1
    return count