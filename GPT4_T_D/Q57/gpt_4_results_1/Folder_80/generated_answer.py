import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    rows, cols = matrix.shape
    for box_row in range(1, rows + 1):
        for box_col in range(1, cols + 1):
            for i in range(rows - box_row + 1):
                for j in range(cols - box_col + 1):
                    submatrix = matrix[i:i + box_row, j:j + box_col]
                    if np.sum(submatrix) == 245:
                        results.append(submatrix.tolist())
    return results