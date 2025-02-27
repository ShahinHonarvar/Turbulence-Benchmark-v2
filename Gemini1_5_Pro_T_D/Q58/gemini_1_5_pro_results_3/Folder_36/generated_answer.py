import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = (len(matrix), len(matrix[0]))
    count = 0
    for i in range(m - 130):
        for j in range(n - 130):
            submatrix = matrix[i:i + 131, j:j + 131]
            if submatrix.size == 131:
                count += 1
    return count