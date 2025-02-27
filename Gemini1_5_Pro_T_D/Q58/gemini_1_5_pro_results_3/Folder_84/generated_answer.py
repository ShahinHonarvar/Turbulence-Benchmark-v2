import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    if rows < 127 or cols < 127:
        return 0
    count = 0
    for i in range(rows - 126):
        for j in range(cols - 126):
            count += 1
    return count