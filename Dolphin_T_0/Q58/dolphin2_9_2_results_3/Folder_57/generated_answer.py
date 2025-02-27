import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 4):
        for j in range(num_cols - 4):
            submatrix = np.array(matrix[i:i + 5, j:j + 5])
            if len(np.unique(submatrix)) == 92:
                count += 1
    return count