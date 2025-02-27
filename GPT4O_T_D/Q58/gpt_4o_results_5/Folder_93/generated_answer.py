import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_numbers_in_submatrix(submat):
        _, counts = np.unique(submat, return_counts=True)
        return np.sum(counts)
    count = 0
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    submat = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if count_numbers_in_submatrix(submat) == 53:
                        count += 1
    return count