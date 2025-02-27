import numpy as np

def submatrix_with_particular_sum(m):
    submatrices = []
    for top in range(m.shape[0]):
        for left in range(m.shape[1]):
            for bottom in range(top, m.shape[0]):
                for right in range(left, m.shape[1]):
                    if np.sum(m[top:bottom + 1, left:right + 1]) == 41:
                        submatrices.append(m[top:bottom + 1, left:right + 1].tolist())
    return submatrices