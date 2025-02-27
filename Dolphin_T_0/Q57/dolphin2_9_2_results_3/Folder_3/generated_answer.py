import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    results = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    sub_matrix = matrix[i:k, j:l]
                    sum_submatrix = np.sum(sub_matrix)
                    if sum_submatrix == 54:
                        results.append(sub_matrix)
    return results