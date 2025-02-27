import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_size = int(np.sqrt(46))
    count = 0
    for i in range(rows - submatrix_size + 1):
        for j in range(cols - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if np.sum(submatrix) == 46:
                count += 1
    return count