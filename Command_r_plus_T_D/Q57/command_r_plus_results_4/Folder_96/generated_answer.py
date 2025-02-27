import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:

    def get_submatrices(matrix, row_start, row_end, col_start, col_end):
        return [matrix[i:j, k:l] for i in range(row_start, row_end + 1) for j in range(i, row_end + 1) for k in range(col_start, col_end + 1) for l in range(k, col_end + 1)]
    target_sum = -63
    num_rows, num_cols = matrix.shape
    result = []
    for row_start in range(num_rows):
        for row_end in range(row_start, num_rows):
            for col_start in range(num_cols):
                for col_end in range(col_start, num_cols):
                    submatrices = get_submatrices(matrix, row_start, row_end, col_start, col_end)
                    for submatrix in submatrices:
                        if np.sum(submatrix) == target_sum:
                            result.append(submatrix)
    return result