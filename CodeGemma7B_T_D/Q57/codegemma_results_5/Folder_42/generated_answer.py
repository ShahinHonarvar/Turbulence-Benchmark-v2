import numpy as np

def submatrix_with_particular_sum(arr):
    """
    Given a numpy array, return all submatrices with a sum of 862.
    """
    max_sum = np.sum(arr)
    result = []
    for matrix in np.split(arr, len(arr)):
        result.append(matrix)
        for matrix in np.split(matrix, len(matrix), axis=0):
            result.append(matrix)
        for matrix in np.split(matrix, len(matrix), axis=1):
            result.append(matrix)
    for matrix in result:
        if np.sum(matrix) == 862:
            return [matrix]
    return []