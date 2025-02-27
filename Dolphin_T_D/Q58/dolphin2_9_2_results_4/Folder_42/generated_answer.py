import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] not in range(193):
                continue
            for x in range(i + 1, rows):
                for y in range(j + 1, cols):
                    if (x - i + 1) * (y - j + 1) * (matrix[x, y] - matrix[i, j]) == 193:
                        count += 1
                    elif (x - i + 1) * (y - j + 1) * (matrix[x, y] - matrix[i, j]) < 193:
                        break
    return count