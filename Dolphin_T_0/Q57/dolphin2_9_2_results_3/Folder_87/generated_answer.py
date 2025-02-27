import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for I in range(i, rows):
                for J in range(j, cols):
                    ind_rows = I - i + 1
                    ind_cols = J - j + 1
                    if ind_rows * ind_cols == 1:
                        sum_ele = matrix[i:I + 1, j:J + 1].sum()
                        if sum_ele == 35:
                            submatrices.append(matrix[i:I + 1, j:J + 1].tolist())
                    elif ind_cols == 1 and np.all(matrix[i:I + 1, j] == 35):
                        submatrices.append(matrix[i:I + 1, j].tolist())
    return submatrices