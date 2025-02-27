import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 33):
        for j in range(cols - 33):
            for k in range(i + 34, rows + 1):
                for l in range(j + 34, cols + 1):
                    if (k - i) * (l - j) == 34:
                        count += 1
    return count