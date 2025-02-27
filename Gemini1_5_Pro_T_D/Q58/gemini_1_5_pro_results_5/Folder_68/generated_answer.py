import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 73):
        for j in range(cols - 73):
            for k in range(i + 74, rows + 1):
                for l in range(j + 74, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.size(submatrix) == 74:
                        count += 1
    return count