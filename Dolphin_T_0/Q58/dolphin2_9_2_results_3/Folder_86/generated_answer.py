import numpy as np

def submatrix_with_n_numbers(matrix):
    result = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 138:
                size = 1
                for m in range(i + 1, rows):
                    for n in range(j + 1, cols):
                        if matrix[m, n] == 138:
                            size += 1
                        else:
                            break
                    if size == 138:
                        result += 1
                    else:
                        break
    return result