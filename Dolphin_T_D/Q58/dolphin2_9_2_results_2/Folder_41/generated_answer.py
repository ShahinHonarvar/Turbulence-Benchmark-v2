import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 73:
                for row in range(i, rows):
                    for col in range(j, cols):
                        submatrix = matrix[i:row + 1, j:col + 1]
                        if np.count_nonzero(submatrix == 73) == 73:
                            count += 1
    return count