import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 17):
        for j in range(cols - 10):
            submatrix = matrix[i:i + 18, j:j + 11]
            if np.size(submatrix) == 186:
                count += 1
    return count