import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 3):
            if j + 3 < cols and i + 2 < rows:
                submatrix = matrix[i:i + 3, j:j + 4]
                if submatrix.size == 13:
                    count += 1
    return count