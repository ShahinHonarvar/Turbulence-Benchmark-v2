import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(matrix, i_start, j_start, i_end, j_end):
        return np.sum(matrix[i_start:i_end, j_start:j_end])
    submatrices = []
    i_max, j_max = matrix.shape
    for i in range(i_max):
        for j in range(j_max):
            for i_end in range(i + 1, i_max + 1):
                for j_end in range(j + 1, j_max + 1):
                    submatrix_sum = sum_submatrix(matrix, i, j, i_end, j_end)
                    if submatrix_sum == -779:
                        submatrices.append(matrix[i:i_end, j:j_end])
    return submatrices if submatrices else []