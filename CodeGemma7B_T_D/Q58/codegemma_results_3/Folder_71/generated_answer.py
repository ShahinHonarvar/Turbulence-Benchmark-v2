from typing import List
import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    count = 0
    for beg_row in range(matrix.shape[0]):
        for end_row in range(beg_row, matrix.shape[0]):
            row_sums = matrix[beg_row:end_row + 1, :].sum(axis=0)
            sums_dict = {0: 1}
            current_sum = 0
            for row_sum in row_sums:
                current_sum += row_sum
                if current_sum in sums_dict:
                    count += sums_dict[current_sum]
                    sums_dict[current_sum] += 1
                else:
                    sums_dict[current_sum] = 1
    return count