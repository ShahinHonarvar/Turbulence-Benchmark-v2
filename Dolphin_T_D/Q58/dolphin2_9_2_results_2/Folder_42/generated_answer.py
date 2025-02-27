import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    length = rows * cols
    submatrices = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                submatrices += 1
                for k in range(i - 1, -1, -1):
                    if np.all(matrix[k, j:j + length] == 0):
                        break
                    else:
                        submatrices -= 1
                for k in range(j - 1, -1, -1):
                    if np.all(matrix[i:i + length, k] == 0):
                        break
                    else:
                        submatrices -= 1
    return submatrices if submatrices >= 193 else 0