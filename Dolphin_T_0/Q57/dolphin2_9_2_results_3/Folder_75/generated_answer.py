import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    ans = []
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    submatrix = np.array(matrix[i:k + 1, j:l + 1])
                    if np.sum(submatrix) == 16:
                        ans.append(submatrix)
    return ans