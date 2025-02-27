import numpy as np

def submatrix_with_n_numbers(matrix):
    output_count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for r in range(row, rows):
                for c in range(col, cols):
                    submatrix = matrix[row:r + 1, col:c + 1]
                    if np.count_nonzero(submatrix == 126) == 126:
                        output_count += 1
    return output_count