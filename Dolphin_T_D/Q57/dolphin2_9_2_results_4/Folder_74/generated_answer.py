import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    sub = matrix[i:x + 1, j:y + 1]
                    if sub.sum() > 88:
                        break
                    elif sub.sum() == 88:
                        submatrices.append(sub.tolist())
    return submatrices