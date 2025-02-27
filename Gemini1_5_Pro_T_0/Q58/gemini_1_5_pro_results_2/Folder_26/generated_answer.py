import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 114):
        for j in range(cols - 114):
            for k in range(i + 115, rows + 1):
                for l in range(j + 115, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.size(submatrix) == 115:
                        count += 1
    return count