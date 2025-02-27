import numpy as np

def submatrix_with_particular_sum(matrix):
    n = len(matrix)
    sum_matrix = np.cumsum(np.cumsum(matrix, axis=0), axis=1)
    submatrices = []
    for x1 in range(n):
        for x2 in range(x1, n):
            for y1 in range(n):
                for y2 in range(y1, n):
                    sum_submatrix = sum_matrix[x2][y2]
                    if x1 > 0:
                        sum_submatrix -= sum_matrix[x1 - 1][y2]
                    if y1 > 0:
                        sum_submatrix -= sum_matrix[x2][y1 - 1]
                    if x1 > 0 and y1 > 0:
                        sum_submatrix += sum_matrix[x1 - 1][y1 - 1]
                    if sum_submatrix == 0:
                        submatrices.append(matrix[x1:x2, y1:y2])
    return submatrices