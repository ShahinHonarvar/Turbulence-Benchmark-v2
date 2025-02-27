import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 2):
            if len(np.unique(matrix[i:i + 3, j:j + 3])) == 1 and len(np.unique(matrix[i, j:j + 3])) == 1 and (len(np.unique(matrix[i + 1, j:j + 3])) == 1) and (len(np.unique(matrix[i + 2, j:j + 3])) == 1) and (len(np.unique(matrix[i:i + 3, j])) == 1) and (len(np.unique(matrix[i:i + 3, j + 1])) == 1) and (len(np.unique(matrix[i:i + 3, j + 2])) == 1):
                submatrix_count += 1
    return submatrix_count