import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            for k in range(i + 1, len(matrix) + 1):
                for l in range(j + 1, len(row) + 1):
                    submatrix = np.array(matrix[i:k, j:l])
                    if np.sum(submatrix) == -61:
                        submatrices.append(submatrix.tolist())
    return submatrices