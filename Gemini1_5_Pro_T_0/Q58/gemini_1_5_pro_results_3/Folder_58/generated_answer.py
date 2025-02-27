import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 17):
        for j in range(cols - 10):
            for k in range(i + 18, rows + 1):
                for l in range(j + 11, cols + 1):
                    if (k - i) * (l - j) == 185:
                        count += 1
    return count