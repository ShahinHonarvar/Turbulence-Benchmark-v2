import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for h1 in range(rows):
        for h2 in range(h1, rows):
            for w1 in range(cols):
                for w2 in range(w1, cols):
                    submatrix = matrix[h1:h2 + 1, w1:w2 + 1]
                    if submatrix.size == 99:
                        count += 1
    return count