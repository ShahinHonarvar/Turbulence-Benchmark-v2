import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(rows, cols, target_size):
        if rows * cols < target_size:
            return 0
        num_elements = rows * cols
        count = 0
        for top in range(rows):
            for left in range(cols):
                for bottom in range(top, rows):
                    for right in range(left, cols):
                        total_elements = (bottom - top + 1) * (right - left + 1)
                        if total_elements == target_size:
                            count += 1
        return count
    rows, cols = matrix.shape
    result = count_submatrices(rows, cols, 115)
    return result