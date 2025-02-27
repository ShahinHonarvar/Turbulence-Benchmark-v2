import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    flat_matrix = matrix.flatten()
    flat_matrix_set = set(flat_matrix)
    for i in range(len(flat_matrix)):
        for j in range(i + 1, len(flat_matrix) + 1):
            subarray = flat_matrix[i:j]
            sum_subarray = np.sum(subarray)
            if sum_subarray == -63:
                indices = [flat_matrix.tolist().index(elem) for elem in subarray]
                submatrix = matrix[indices[0] // matrix.shape[1], indices[0] % matrix.shape[1]:indices[-1] // matrix.shape[1], indices[-1] % matrix.shape[1] + 1]
                submatrices.append(submatrix)
    return submatrices