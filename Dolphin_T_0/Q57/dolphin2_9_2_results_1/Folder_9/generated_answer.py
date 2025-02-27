import numpy as np

def submatrix_with_particular_sum(mat):
    i, j, n, m = (0, 0, len(mat), len(mat[0]))
    mat_sum = np.cumsum(np.cumsum(mat, 0), 1)
    sub_matrices = set()
    for i in range(n):
        for j in range(m):
            for n in range(i + 1, n + 1):
                for m in range(j + 1, m + 1):
                    if mat_sum[n - 1, m - 1] - mat_sum[i, m - 1] - mat_sum[n - 1, j - 1] + mat_sum[i, j - 1] == -86:
                        sub_matrices.add((i, j, n, m))
    return list(sub_matrices)