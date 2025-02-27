import numpy as np

def submatrix_with_n_numbers(matrix, n=103):
    h, w = matrix.shape
    count = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                for x in range(i + 1, h + 1):
                    for y in range(j + 1, w + 1):
                        submatrix = matrix[i:x, j:y]
                        if len(submatrix.flatten()) == n:
                            count += 1
    return count