import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 5):
        for j in range(cols - 9):
            for k in range(i + 6, rows + 1):
                for l in range(j + 10, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.size(submatrix) == 60:
                        count += 1
    return count