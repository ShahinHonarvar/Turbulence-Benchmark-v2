import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = (len(matrix), len(matrix[0]))
    count = 0
    for i in range(m - 99 + 1):
        for j in range(n - 99 + 1):
            submatrix = matrix[i:i + 99, j:j + 99]
            if submatrix.size == 99:
                count += 1
    return count