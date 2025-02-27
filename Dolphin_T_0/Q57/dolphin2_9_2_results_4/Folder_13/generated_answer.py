import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return []
    submatrix_list = []
    row_num, col_num = matrix.shape
    for i in range(row_num):
        for j in range(col_num):
            for x in range(i + 1, row_num + 1):
                for y in range(j + 1, col_num + 1):
                    sub_matrix = matrix[i:x, j:y]
                    if np.sum(sub_matrix) == 382:
                        submatrix_list.append(sub_matrix)
    return submatrix_list