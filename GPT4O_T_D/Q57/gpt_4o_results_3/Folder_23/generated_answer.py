import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(arr, target):
        r, c = arr.shape
        submatrices = []
        for start_row in range(r):
            for start_col in range(c):
                for end_row in range(start_row, r):
                    for end_col in range(start_col, c):
                        submatrix = arr[start_row:end_row + 1, start_col:end_col + 1]
                        if np.sum(submatrix) == target:
                            submatrices.append(submatrix)
        return submatrices
    return find_submatrices_with_sum(matrix, 59)