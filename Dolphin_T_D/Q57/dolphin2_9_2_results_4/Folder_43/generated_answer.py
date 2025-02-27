import numpy as np

def submatrix_with_particular_sum(mat):
    row_num, col_num = mat.shape
    ans = []
    for i in range(row_num):
        for j in range(col_num):
            for k in range(i + 1, row_num):
                for l in range(j + 1, col_num):
                    if mat[k - 1:i + 1, l - 1:j + 1].sum() == -81:
                        ans.append(mat[k - 1:i + 1, l - 1:j + 1].tolist())
    return ans