import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for i_end in range(i + 1, rows + 1):
                for j_end in range(j + 1, cols + 1):
                    submatrix = matrix[i:i_end, j:j_end]
                    if submatrix.sum() == -394:
                        result.append(submatrix)
    return result