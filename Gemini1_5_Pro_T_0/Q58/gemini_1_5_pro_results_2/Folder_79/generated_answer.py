import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 5):
        for j in range(cols - 5):
            for k in range(i + 6, rows + 1):
                for l in range(j + 6, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size == 60:
                        count += 1
    return count