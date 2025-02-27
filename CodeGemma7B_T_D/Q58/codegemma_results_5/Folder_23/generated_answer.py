import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            for r in range(row, len(matrix)):
                for c in range(col, len(matrix)):
                    submatrix = matrix[r, c] - matrix[row - 1, c] - matrix[r, col - 1] + matrix[row - 1, col - 1]
                    if np.sum(submatrix == 69) == 69:
                        count += 1
    return count