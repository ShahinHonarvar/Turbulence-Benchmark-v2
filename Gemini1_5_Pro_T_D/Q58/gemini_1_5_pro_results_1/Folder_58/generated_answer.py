import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 17):
        for j in range(cols - 11):
            for k in range(i + 18, rows + 1):
                for l in range(j + 12, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size == 185:
                        count += 1
    return count