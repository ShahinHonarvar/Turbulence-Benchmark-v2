import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 46:
                if i + 46 <= rows and j + 46 <= cols:
                    submatrix = matrix[i:i + 46, j:j + 46]
                    if np.count_nonzero(submatrix == 46) == 46:
                        count += 1
    return count