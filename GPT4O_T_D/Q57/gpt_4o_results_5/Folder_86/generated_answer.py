import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_sum_submatrix(i, j, k, l):
        return np.sum(matrix[i:k + 1, j:l + 1])
    submatrix_list = []
    rows, cols = matrix.shape
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if get_sum_submatrix(top, left, bottom, right) == -394:
                        submatrix_list.append(matrix[top:bottom + 1, left:right + 1].tolist())
    return submatrix_list