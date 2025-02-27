import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 94):
        for j in range(cols - 94):
            submatrix = matrix[i:i + 95, j:j + 95]
            if np.size(submatrix) == 9025:
                count += 1
    return count