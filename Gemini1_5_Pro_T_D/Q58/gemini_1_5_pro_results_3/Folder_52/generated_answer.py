import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            if i + 3 <= rows and j + 3 <= cols:
                submatrix = matrix[i:i + 3, j:j + 3]
                if np.size(submatrix) == 147:
                    count += 1
    return count