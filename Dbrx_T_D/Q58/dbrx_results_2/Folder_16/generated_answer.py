import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(matrix.shape[0] - 2):
        for col in range(matrix.shape[1] - 2):
            submatrix = matrix[row:row + 3, col:col + 3]
            if np.isin(submatrix, 154).all():
                count += 1
    return count