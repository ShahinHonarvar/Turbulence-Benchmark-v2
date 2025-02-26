import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for height in range(1, rows - i + 1):
                for width in range(1, cols - j + 1):
                    submatrix = matrix[i:i + height, j:j + width]
                    if np.unique(submatrix).size == 2:
                        count += 1
    return count