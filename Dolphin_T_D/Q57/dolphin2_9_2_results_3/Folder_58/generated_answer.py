import numpy as np

def submatrix_with_particular_sum(mat):
    nrows = mat.shape[0]
    ncols = mat.shape[1]
    submatrices = []
    for r1 in range(nrows):
        for r2 in range(r1, nrows):
            for c1 in range(ncols):
                for c2 in range(c1, ncols):
                    if r1 != r2 and c1 != c2:
                        submat = mat[r1:r2 + 1, c1:c2 + 1]
                        if submat.sum() == -137:
                            submatrices.append(submat.tolist())
    return submatrices