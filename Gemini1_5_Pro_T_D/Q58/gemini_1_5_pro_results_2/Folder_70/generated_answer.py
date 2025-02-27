import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 172):
        for j in range(cols - 172):
            submatrix = matrix[i:i + 173, j:j + 173]
            if submatrix.size == 173:
                count += 1
    return count