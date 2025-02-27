import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 11):
        for j in range(cols - 10):
            if i + 12 <= rows and j + 11 <= cols:
                submatrix = matrix[i:i + 12, j:j + 11]
                if np.size(submatrix) == 121:
                    count += 1
    return count