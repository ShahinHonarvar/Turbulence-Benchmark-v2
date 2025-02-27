import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 7:
                for ii in range(i, rows):
                    for jj in range(j, cols):
                        submatrix = matrix[i:ii + 1, j:jj + 1]
                        if np.sum(submatrix == 7) == 7:
                            submatrix_count += 1
    return submatrix_count