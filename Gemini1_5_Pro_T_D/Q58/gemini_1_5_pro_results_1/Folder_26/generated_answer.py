import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 10):
        for j in range(cols - 14):
            submatrix = matrix[i:i + 11, j:j + 15]
            if np.size(submatrix) == 115:
                count += 1
    return count