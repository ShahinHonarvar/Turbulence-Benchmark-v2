import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:

    def get_submatrices(matrix, row_start, row_end, col_start, col_end):
        return [matrix[i:j, k:l] for i in range(row_start, row_end + 1) for j in range(i, row_end + 1) for k in range(col_start, col_end + 1) for l in range(k, col_end + 1)]

    def check_submatrix_sum(submatrix):
        return np.sum(submatrix) == -38
    row_length, col_length = matrix.shape
    all_submatrices = []
    for row_start in range(row_length):
        for row_end in range(row_start, row_length):
            for col_start in range(col_length):
                for col_end in range(col_start, col_length):
                    submatrices = get_submatrices(matrix, row_start, row_end, col_start, col_end)
                    all_submatrices.extend([sub for sub in submatrices if check_submatrix_sum(sub)])
    return all_submatrices