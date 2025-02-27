import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for i in range(rows - 2):
        for j in range(columns - 2):
            sub = matrix[i:i + 3, j:j + 3]
            if len(sub[sub == 7]) == 7:
                count += 1
    return count