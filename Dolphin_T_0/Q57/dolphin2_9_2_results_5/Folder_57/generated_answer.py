import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrix_list = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.sum(submatrix) == 13:
                submatrix_list.append(submatrix)
    return submatrix_list