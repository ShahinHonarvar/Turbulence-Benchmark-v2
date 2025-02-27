import numpy as np

def submatrix_with_particular_sum(mat):
    sum_val = 27
    rows = len(mat)
    cols = len(mat[0])
    all_submatrices = []
    for i in range(rows):
        for j in range(cols):
            for size in range(2, min(rows - i + 1, cols - j + 1) + 1):
                submatrix_sum = np.sum(mat[i:i + size, j:j + size])
                if submatrix_sum == sum_val:
                    all_submatrices.append(mat[i:i + size, j:j + size])
    return all_submatrices