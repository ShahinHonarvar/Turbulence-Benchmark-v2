import numpy as np

def submatrix_with_n_numbers(mat):
    out = 0
    for top in range(mat.shape[0]):
        for down in range(top, mat.shape[0]):
            for left in range(mat.shape[1]):
                for right in range(left, mat.shape[1]):
                    subm = mat[top:down + 1, left:right + 1]
                    if np.count_nonzero(subm == 127) == 127:
                        out += 1
    return out