import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:

    def get_submatrix(i, j, rows, cols):
        return matrix[i:i + rows, j:j + cols]
    rows, cols = matrix.shape
    result = []
    for rows_count in range(1, rows + 1):
        for cols_count in range(1, cols + 1):
            for i in range(rows - rows_count + 1):
                for j in range(cols - cols_count + 1):
                    submatrix = get_submatrix(i, j, rows_count, cols_count)
                    if np.sum(submatrix) == 21:
                        result.append(submatrix)
    return result