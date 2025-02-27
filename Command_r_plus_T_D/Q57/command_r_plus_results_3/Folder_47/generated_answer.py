import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list[np.ndarray]:

    def find_submatrices(row_start, col_start, target_sum):
        if target_sum == 0:
            return [np.array([])]
        if row_start == matrix.shape[0] or col_start == matrix.shape[1]:
            return []
        submatrices = []
        for row_end in range(row_start, matrix.shape[0]):
            for col_end in range(col_start, matrix.shape[1]):
                submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                submatrix_sum = np.sum(submatrix)
                remaining_sum = target_sum - submatrix_sum
                if remaining_sum == 0:
                    submatrices.append(submatrix)
                elif remaining_sum > 0:
                    submatrices_in_remaining = find_submatrices(row_end + 1, col_end + 1, remaining_sum)
                    submatrices.extend(submatrices_in_remaining)
        return submatrices
    all_submatrices = find_submatrices(0, 0, 27)
    return all_submatrices