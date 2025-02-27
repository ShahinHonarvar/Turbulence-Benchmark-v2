import numpy as np

def submatrix_with_particular_sum(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    result = []
    for i in range(rows):
        for j in range(cols):
            for k1 in range(i + 1, rows + 1):
                for k2 in range(j + 1, cols + 1):
                    sub_array = matrix[i:k1, j:k2]
                    if sub_array.sum() == -86:
                        result.append(sub_array)
    return result