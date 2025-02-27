import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for end_col in range(j, cols):
                    submatrix = matrix[i:k + 1, j:end_col + 1]
                    if np.size(submatrix) == 104:
                        count += 1
    return count