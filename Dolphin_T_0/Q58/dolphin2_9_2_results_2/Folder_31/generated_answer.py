import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 44):
        for j in range(matrix.shape[1] - 44):
            if np.all(matrix[i:i + 45, j:j + 45] == 45):
                count += 1
    return count