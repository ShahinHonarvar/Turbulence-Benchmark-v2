import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n_rows, n_cols = matrix.shape
    n = 185
    n_sqrt = int(np.ceil(np.sqrt(n)))
    for i in range(n_rows - n_sqrt + 1):
        for j in range(n_cols - n_sqrt + 1):
            submatrix = matrix[i:i + n_sqrt, j:j + n_sqrt]
            for k in range(n_sqrt):
                for start_row in range(n_sqrt - k):
                    for start_col in range(n_sqrt - k):
                        submatrix_size = (start_row + k + 1) * (start_col + k + 1)
                        if submatrix_size == n:
                            count += 1
    return count