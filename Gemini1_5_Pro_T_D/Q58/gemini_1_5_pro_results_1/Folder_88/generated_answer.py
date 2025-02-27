import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 66):
        for j in range(cols - 66):
            for k in range(i + 67, rows + 1):
                for l in range(j + 67, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.size(submatrix) == 67:
                        count += 1
    return count