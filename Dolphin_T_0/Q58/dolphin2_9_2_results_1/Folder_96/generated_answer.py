import numpy

def submatrix_with_n_numbers(matrix):
    n = 20
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + n, rows):
                for l in range(j + n, cols):
                    if (k - i + 1) * (l - j + 1) == n:
                        count += 1
    return count