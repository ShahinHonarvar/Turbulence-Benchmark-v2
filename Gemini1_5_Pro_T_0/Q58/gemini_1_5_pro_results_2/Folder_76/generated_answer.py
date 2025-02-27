import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 14):
        for j in range(cols - 8):
            if i + 15 <= rows and j + 9 <= cols:
                submatrix = matrix[i:i + 15, j:j + 9]
                if np.size(submatrix) == 159:
                    count += 1
    return count