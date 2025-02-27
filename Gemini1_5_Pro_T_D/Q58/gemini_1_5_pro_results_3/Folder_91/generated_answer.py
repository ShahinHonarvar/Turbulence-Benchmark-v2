import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            for k in range(i + 2, rows + 1):
                for l in range(j + 2, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size == 5:
                        count += 1
    return count