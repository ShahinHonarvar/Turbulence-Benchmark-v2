import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    flat_matrix = matrix.flatten()
    for i in range(flat_matrix.shape[0]):
        for j in range(i + 1, flat_matrix.shape[0] + 1):
            if np.sum(flat_matrix[i:j]) == 95:
                submatrix = flat_matrix[i:j].reshape(-1, int(np.sqrt(j - i)))
                submatrices.append(submatrix)
    return submatrices