import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for r in range(rows - 1):
        for c in range(columns - 1):
            submatrix = matrix[r:r + 2, c:c + 2]
            if len(submatrix[submatrix == 47].tolist()) == 4:
                count += 1
    return count