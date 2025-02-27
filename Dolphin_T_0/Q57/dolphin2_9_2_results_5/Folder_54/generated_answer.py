import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sub = matrix[i:k + 1, j:l + 1]
                    sum_sub = np.sum(sub)
                    if sum_sub == -59:
                        submatrices.append([sub.tolist()])
    return submatrices