import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if r * c == 185:
                for i in range(rows - r + 1):
                    for j in range(cols - c + 1):
                        submatrix = matrix[i:i + r, j:j + c]
                        if submatrix.size == 185:
                            count += 1
    return count