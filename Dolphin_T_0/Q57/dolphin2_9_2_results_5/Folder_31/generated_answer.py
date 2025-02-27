import numpy as np

def submatrix_with_particular_sum(mat):
    result = []
    rows, cols = mat.shape
    for i in range(rows):
        for j in range(cols):
            for x in range(i + 1, rows + 1):
                for y in range(j + 1, cols + 1):
                    submat = mat[i:x, j:y]
                    if np.sum(submat) == -44:
                        result.append(submat.tolist())
    return result