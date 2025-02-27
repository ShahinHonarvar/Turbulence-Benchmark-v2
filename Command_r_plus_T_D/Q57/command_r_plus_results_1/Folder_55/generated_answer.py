import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:

    def get_submatrices(matrix, row_start, row_end, col_start, col_end):
        submatrices = []
        for i in range(row_start, row_end + 1):
            for j in range(col_start, col_end + 1):
                submatrix = matrix[i, j]
                submatrices.append(submatrix)
        return submatrices

    def check_submatrix_sum(submatrices):
        return sum(submatrices) == 1
    row_length, col_length = matrix.shape
    all_submatrices = []
    for row_start in range(row_length):
        for row_end in range(row_start, row_length):
            for col_start in range(col_length):
                for col_end in range(col_start, col_length):
                    submatrices = get_submatrices(matrix, row_start, row_end, col_start, col_end)
                    if check_submatrix_sum(submatrices):
                        all_submatrices.append(submatrices)
    return all_submatrices