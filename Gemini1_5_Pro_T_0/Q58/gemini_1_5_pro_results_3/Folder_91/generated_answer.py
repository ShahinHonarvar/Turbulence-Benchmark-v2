import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            for k in range(i + 1, rows):
                for l in range(j + 1, cols):
                    if (k - i + 1) * (l - j + 1) == 5:
                        count += 1
    return count