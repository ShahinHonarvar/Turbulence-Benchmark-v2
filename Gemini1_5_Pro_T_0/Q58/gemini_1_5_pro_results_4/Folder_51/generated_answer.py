import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            for k in range(i + 3, rows + 1):
                for l in range(j + 3, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.size(submatrix) == 95:
                        count += 1
    return count