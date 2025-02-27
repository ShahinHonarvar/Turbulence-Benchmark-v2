import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 91):
        for j in range(cols - 91):
            submatrix = matrix[i:i + 92, j:j + 92]
            if submatrix.size == 92:
                count += 1
    return count