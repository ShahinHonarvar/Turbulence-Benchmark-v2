import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    submatrices = []
    for i in range(nrows):
        for j in range(ncols):
            m1, m2, m3 = (np.tril(matrix[i:, j:] - matrix[i, j]).sum(), np.triu(matrix[i:, j:] - matrix[i, j]).sum(), np.tril(matrix[i:, j:] - matrix[i, j]).sum() - matrix[i, j])
            if m1 == 77:
                submatrices.append(matrix[i:i + int(np.sqrt(2 * m1 + 0.25) - 0.5) + 1, j:j + int(np.sqrt(2 * m1 + 0.25) - 0.5) + 1])
            if m2 == 77:
                submatrices.append(matrix[i:i + int(np.sqrt(2 * m2 + 0.25) - 0.5) + 1, j:j + int(np.sqrt(2 * m2 + 0.25) - 0.5) + 1])
            if m3 == 77:
                submatrices.append(matrix[i:i + int(np.sqrt(2 * m3 + 0.25) - 0.5) + 1, j:j + int(np.sqrt(2 * m3 + 0.25) - 0.5) + 1])
    return submatrices