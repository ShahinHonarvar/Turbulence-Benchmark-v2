import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 79):
        for j in range(cols - 79):
            for k in range(i + 80, rows + 1):
                for l in range(j + 80, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size == 80:
                        count += 1
    return count