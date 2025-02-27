import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for subrow in range(row + 1, rows + 1):
                for subcol in range(col + 1, cols + 1):
                    submatrix = matrix[row:subrow, col:subcol]
                    if np.sum(submatrix) == -617:
                        result.append(submatrix.tolist())
    return result