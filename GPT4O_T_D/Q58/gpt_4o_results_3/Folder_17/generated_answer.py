import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    rows, cols = matrix.shape
    total_count = 0
    if rows * cols < 166:
        return 0
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if r * c == 166:
                for i in range(rows - r + 1):
                    for j in range(cols - c + 1):
                        submatrix = matrix[i:i + r, j:j + c]
                        if submatrix.size == 166:
                            total_count += 1
    return total_count