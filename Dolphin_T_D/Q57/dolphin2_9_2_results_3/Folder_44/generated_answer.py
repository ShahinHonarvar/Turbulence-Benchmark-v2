import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    total_rows, total_cols = matrix.shape
    for i in range(total_rows):
        for j in range(total_cols):
            for x in range(i, total_rows):
                for y in range(j, total_cols):
                    submatrix_sum = np.sum(matrix[i:x + 1, j:y + 1])
                    if submatrix_sum == 830:
                        submatrix = matrix[i:x + 1, j:y + 1]
                        submatrices.append(submatrix)
    return submatrices