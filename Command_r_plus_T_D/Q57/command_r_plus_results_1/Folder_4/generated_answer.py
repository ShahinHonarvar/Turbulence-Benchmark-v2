import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:

    def get_submatrices(matrix, row_start, row_end, col_start, col_end):
        return [matrix[i:j, k:l] for i in range(row_start, row_end + 1) for j in range(i, row_end + 1) for k in range(col_start, col_end + 1) for l in range(k, col_end + 1)]
    result = []
    rows, cols = matrix.shape
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    submatrices = get_submatrices(matrix, row_start, row_end, col_start, col_end)
                    for submatrix in submatrices:
                        if np.sum(submatrix) == 87:
                            result.append(submatrix)
    return result