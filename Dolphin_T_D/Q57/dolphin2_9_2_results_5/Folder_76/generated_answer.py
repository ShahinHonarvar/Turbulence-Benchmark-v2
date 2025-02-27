import numpy as np

def submatrix_with_particular_sum(matrix):
    flat = matrix.flatten()
    indices = np.argwhere(flat == -255)
    values = flat[indices]
    submatrix_list = []
    for i, val in zip(indices, values):
        if val == -255:
            sub_matrix = matrix[i[1]:i[2] + 1, i[0]:i[3] + 1]
            submatrix_list.append(sub_matrix.tolist())
    if len(submatrix_list) == 0:
        return []
    else:
        return submatrix_list