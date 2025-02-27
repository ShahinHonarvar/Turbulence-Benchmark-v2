import numpy as np

def submatrix_with_particular_sum(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            for k in range(i + 1, m.shape[0]):
                for l in range(j + 1, m.shape[1]):
                    submatrix = m[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 99:
                        return submatrix
    return []