import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 27):
        for j in range(cols - 27):
            submatrix = matrix[i:i + 28, j:j + 28]
            if submatrix.size == 784:
                count += 1
    return count