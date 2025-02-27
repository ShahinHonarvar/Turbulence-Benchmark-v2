import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_values = -64
    rows, cols = matrix.shape
    submatrix = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sub = np.array(matrix[i:k + 1, j:l + 1])
                    if sum(sub.flatten()) == sum_values:
                        submatrix.append(sub)
    return submatrix