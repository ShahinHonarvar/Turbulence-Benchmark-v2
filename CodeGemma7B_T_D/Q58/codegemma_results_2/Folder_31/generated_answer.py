import numpy as np

def submatrix_with_n_numbers(mat):
    n = mat.shape[0]
    m = mat.shape[1]
    count = 0
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix = mat[i:k + 1, j:l + 1]
                    if submatrix.size == 45 and np.sum(submatrix) == 45:
                        count += 1
    return count