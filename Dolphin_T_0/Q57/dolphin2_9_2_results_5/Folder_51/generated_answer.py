import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    h, w = matrix.shape
    for h_index in range(h):
        for w_index in range(w):
            for h_size in range(h - h_index + 1):
                for w_size in range(w - w_index + 1):
                    if np.sum(matrix[h_index:h_index + h_size, w_index:w_index + w_size]) == -46:
                        result.append(matrix[h_index:h_index + h_size, w_index:w_index + w_size].tolist())
    return result