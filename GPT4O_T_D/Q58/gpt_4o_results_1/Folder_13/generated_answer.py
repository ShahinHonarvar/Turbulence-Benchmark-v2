import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    total_numbers = 175
    submatrix_size_found = False
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if r * c == total_numbers:
                submatrix_size_found = True
                for i in range(rows - r + 1):
                    for j in range(cols - c + 1):
                        submatrix_count += 1
    if not submatrix_size_found:
        return 0
    return submatrix_count