import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        matrix = np.array(matrix)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for h in range(1, rows - i + 1):
                for w in range(1, cols - j + 1):
                    submatrix = matrix[i:i + h, j:j + w]
                    if submatrix.size == 5:
                        count += 1
    return count