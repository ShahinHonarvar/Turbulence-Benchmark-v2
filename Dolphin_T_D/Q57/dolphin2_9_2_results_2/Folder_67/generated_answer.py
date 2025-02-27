import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, columns = matrix.shape
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(columns):
                for c2 in range(c1, columns):
                    submatrix = np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
                    if submatrix == 40:
                        result.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return result