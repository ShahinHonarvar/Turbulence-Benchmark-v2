import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            submatrix = matrix[i:i + 2, j:j + 4] if j + 4 <= cols else []
            if submatrix.size == 8:
                count += 1
            submatrix = matrix[i:i + 4, j:j + 2] if i + 4 <= rows else []
            if submatrix.size == 8:
                count += 1
    return count