import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for r in range(row, len(matrix)):
                for c in range(col, len(matrix[0])):
                    submatrix = matrix[row:r + 1, col:c + 1]
                    if np.size(submatrix) == 18:
                        count += 1
    return count