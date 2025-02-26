import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for r in range(i, rows):
                for c in range(j, cols):
                    submatrix = matrix[i:r + 1, j:c + 1]
                    if submatrix.size == 24:
                        count += 1
    return count