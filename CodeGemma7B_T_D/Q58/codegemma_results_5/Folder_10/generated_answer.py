import numpy as np

def submatrix_with_n_numbers(M):
    count = 0
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            for k in range(i, M.shape[0]):
                for l in range(j, M.shape[1]):
                    submatrix = M[i:k + 1, j:l + 1]
                    if np.unique(submatrix).size == 56:
                        count += 1
    return count