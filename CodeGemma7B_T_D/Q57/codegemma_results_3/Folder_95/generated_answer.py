import numpy as np

def submatrix_with_particular_sum(matrix):
    ans = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == 19:
                        ans.append(list(matrix[i:k + 1, j:l + 1].tolist()))
    return ans