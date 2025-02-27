import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for i_end in range(i + 1, rows + 1):
                for j_end in range(j + 1, cols + 1):
                    submatrix_sum = np.sum(matrix[i:i_end, j:j_end])
                    if submatrix_sum == -83:
                        submatrices.append(matrix[i:i_end, j:j_end])
    return submatrices