import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 66
    for row in range(rows - int(np.sqrt(n)) + 1):
        for col in range(cols - int(np.sqrt(n)) + 1):
            for sub_rows in range(int(np.sqrt(n)), rows - row + 1):
                for sub_cols in range(int(np.sqrt(n)), cols - col + 1):
                    submatrix = matrix[row:row + sub_rows, col:col + sub_cols]
                    if np.prod(submatrix.shape) == n:
                        count += 1
    return count