import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    r, c = matrix.shape
    for i in range(r):
        for j in range(c):
            for k in range(i, r):
                for h in range(j, c):
                    sub_matrix = matrix[i:k + 1, j:h + 1]
                    if np.sum(sub_matrix) == 80:
                        result.append(sub_matrix)
    return result