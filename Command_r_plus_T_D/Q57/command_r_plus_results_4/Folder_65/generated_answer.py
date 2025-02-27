import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:

    def get_submatrices(row_start, row_end, col_start, col_end):
        return matrix[row_start:row_end, col_start:col_end]
    rows, cols = matrix.shape
    result = []
    for row_start in range(rows):
        for row_end in range(row_start + 1, rows + 1):
            for col_start in range(cols):
                for col_end in range(col_start + 1, cols + 1):
                    submatrix = get_submatrices(row_start, row_end, col_start, col_end)
                    if np.sum(submatrix) == 78:
                        result.append(submatrix)
    return result