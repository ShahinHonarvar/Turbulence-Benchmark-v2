import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = (len(matrix), len(matrix[0]))
    count = 0
    for i in range(rows - 174):
        for j in range(cols - 174):
            for k in range(i + 175, rows + 1):
                for l in range(j + 175, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size == 175:
                        count += 1
    return count