import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_2d_subarray(arr, top, left, bottom, right):
        subarray_sum = np.sum(arr[top:bottom + 1, left:right + 1])
        return subarray_sum
    rows, cols = matrix.shape
    result = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if sum_2d_subarray(matrix, top, left, bottom, right) == -157:
                        submatrix = matrix[top:bottom + 1, left:right + 1]
                        result.append(submatrix)
    return result