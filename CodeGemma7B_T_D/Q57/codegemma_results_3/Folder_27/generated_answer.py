import numpy as np

def submatrix_with_particular_sum(arr):
    res = []
    sum_of_columns = np.sum(arr, axis=0)
    for i in range(len(arr)):
        for j in range(len(arr)):
            col_indices = list(range(j, len(sum_of_columns)))
            for k in range(i, len(arr)):
                row_indices = list(range(i, k + 1))
                if np.sum(arr[row_indices, col_indices]) == 77:
                    res.append(arr[row_indices, col_indices])
    return res