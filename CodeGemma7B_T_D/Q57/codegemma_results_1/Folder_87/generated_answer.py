import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = mat[i:k + 1, j:l + 1]
                    submatrix_sum = np.sum(submatrix)
                    if submatrix_sum == 35:
                        submatrix_list = submatrix.tolist()
                        result.append(submatrix_list)
    return result