import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 42):
        for j in range(cols - 42):
            for k in range(i + 1, rows - 41):
                for l in range(j + 1, cols - 41):
                    if (k - i + 1) * (l - j + 1) == 43:
                        count += 1
    return count