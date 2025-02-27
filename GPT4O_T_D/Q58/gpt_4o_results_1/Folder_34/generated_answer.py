import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    num_count = 0
    for i in range(rows):
        for j in range(cols):
            for p in range(i, rows):
                for q in range(j, cols):
                    submat = matrix[i:p + 1, j:q + 1]
                    if submat.size == 83:
                        num_count += 1
    return num_count