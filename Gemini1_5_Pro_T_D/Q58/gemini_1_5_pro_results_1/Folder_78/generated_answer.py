import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 8):
        for j in range(cols - 12):
            for k in range(i + 9, rows + 1):
                for l in range(j + 13, cols + 1):
                    if (k - i) * (l - j) == 91:
                        count += 1
    return count