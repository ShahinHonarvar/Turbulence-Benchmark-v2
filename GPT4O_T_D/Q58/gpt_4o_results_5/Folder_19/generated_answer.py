import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    required_elements = 17
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if r * c == required_elements:
                for i in range(rows - r + 1):
                    for j in range(cols - c + 1):
                        submatrix = matrix[i:i + r, j:j + c]
                        if submatrix.size == required_elements:
                            count += 1
    return count