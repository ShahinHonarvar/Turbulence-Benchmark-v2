import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 66):
        for j in range(cols - 66):
            submatrix = matrix[i:i + 67, j:j + 67]
            if np.size(submatrix) == 67:
                count += 1
    return count