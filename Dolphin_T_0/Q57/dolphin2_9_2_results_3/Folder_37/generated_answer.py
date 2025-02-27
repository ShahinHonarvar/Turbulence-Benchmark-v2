import numpy as np

def submatrix_with_particular_sum(arr):
    submatrices = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for row in range(i, len(arr)):
                for col in range(j, len(arr[0])):
                    sub = arr[i:row, j:col]
                    if np.sum(sub) == -82:
                        submatrices.append(sub.tolist())
    return submatrices