import numpy as np

def submatrix_with_n_numbers(matrix, n=130):
    rows, cols = matrix.shape
    count = 0
    for x in range(rows):
        for y in range(cols):
            for w in range(y, cols):
                for h in range(x, rows):
                    submatrix = matrix[x:h + 1, y:w + 1]
                    if submatrix.size == n:
                        count += 1
    return count