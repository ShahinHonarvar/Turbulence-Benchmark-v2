import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrices_count = 0
    layer_matrix = np.concatenate([matrix, np.zeros((matrix.shape[0], 1)), np.zeros((1, matrix.shape[1] + 1))], axis=0)
    layer_matrix = np.concatenate([layer_matrix, np.zeros((1, matrix.shape[1] + 1))], axis=0)
    for i in range(1, layer_matrix.shape[0] - 1):
        for j in range(1, layer_matrix.shape[1] - 1):
            if layer_matrix[i, j] != 0:
                if layer_matrix[i - 1, j - 1] == 0 and layer_matrix[i - 1, j] == 0 and (layer_matrix[i - 1, j + 1] == 0):
                    if layer_matrix[i, j - 1] == 0 and layer_matrix[i, j + 1] == 0:
                        if layer_matrix[i + 1, j - 1] == 0 and layer_matrix[i + 1, j] == 0 and (layer_matrix[i + 1, j + 1] == 0):
                            submatrices_count += 1
    return submatrices_count