import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    prefix_sums = np.zeros((matrix.shape[0] + 1, matrix.shape[1] + 1))
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            prefix_sums[row + 1, col + 1] = prefix_sums[row, col + 1] + prefix_sums[row + 1, col] - prefix_sums[row, col] + matrix[row, col]
    res = []
    for top_row, bot_row, left_col, right_col in product(*zip(range(matrix.shape[0]), range(matrix.shape[0]), range(matrix.shape[1]), range(matrix.shape[1]))):
        submatrix_sum = prefix_sums[bot_row + 1, right_col + 1] - prefix_sums[top_row, right_col + 1] - prefix_sums[bot_row + 1, left_col] + prefix_sums[top_row, left_col]
        if submatrix_sum == -26:
            res.append(matrix[top_row:bot_row + 1, left_col:right_col + 1])
    return res