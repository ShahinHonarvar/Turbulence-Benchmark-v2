import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    num_rows = matrix.shape[0]
    num_cols = matrix.shape[1]
    for i in range(num_rows):
        for j in range(num_cols):
            for h in range(i + 1, num_rows):
                for w in range(j + 1, num_cols):
                    submatrix_sum = np.sum(matrix[i:h + 1, j:w + 1])
                    if submatrix_sum == -61:
                        submatrices.append(matrix[i:h + 1, j:w + 1])
    return submatrices