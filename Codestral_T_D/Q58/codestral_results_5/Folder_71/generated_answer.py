import numpy as np

def submatrix_with_n_numbers(matrix, n=78):
    rows, cols = matrix.shape
    count = 0
    for x in range(rows):
        for y in range(cols):
            for i in range(rows - x + 1):
                for j in range(cols - y + 1):
                    submatrix = matrix[x:x + i, y:y + j]
                    if submatrix.size == n:
                        count += 1
    return count