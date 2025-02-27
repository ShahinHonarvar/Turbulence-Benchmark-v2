import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 6):
        for j in range(cols - 6):
            for k in range(i + 7, rows + 1):
                for l in range(j + 7, cols + 1):
                    if (k - i) * (l - j) == 77:
                        count += 1
    return count