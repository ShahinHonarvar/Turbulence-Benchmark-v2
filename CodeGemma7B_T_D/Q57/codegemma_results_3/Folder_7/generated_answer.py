import numpy as np

def submatrix_with_particular_sum(a):
    out = []
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            for ii in range(i, a.shape[0]):
                for jj in range(j, a.shape[1]):
                    if np.sum(a[i:ii + 1, j:jj + 1]) == -128:
                        out.append([i, j, ii, jj])
    return out if out else []