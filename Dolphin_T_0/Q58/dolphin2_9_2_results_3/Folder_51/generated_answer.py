import numpy as np

def submatrix_with_n_numbers(matrix):
    indices = np.where(matrix == 95)
    submatrix_count = 0
    for i in range(len(indices[0])):
        for j in range(i + 1, len(indices[0])):
            submatrix = matrix[indices[0][i]:indices[0][j] + 1, indices[1][i]:indices[1][j] + 1]
            if np.count_nonzero(submatrix == 95) == 95:
                submatrix_count += 1
    if submatrix_count == 0:
        return 0
    else:
        return submatrix_count