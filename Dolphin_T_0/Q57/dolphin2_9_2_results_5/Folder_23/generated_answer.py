import numpy as np

def find_submatrix_with_particular_sum(matrix):
    h_sum = np.cumsum(matrix, axis=0)
    v_sum = np.cumsum(matrix, axis=1)
    submatrices = []
    for x1 in range(matrix.shape[0]):
        for x2 in range(x1 + 1, matrix.shape[0] + 1):
            for y1 in range(matrix.shape[1]):
                for y2 in range(y1 + 1, matrix.shape[1] + 1):
                    sum_submatrix = h_sum[x2, y2] - h_sum[x2, y1] - v_sum[x1, y2] + v_sum[x1, y1]
                    if sum_submatrix == 59:
                        submatrices.append(matrix[x1:x2, y1:y2])
    return submatrices