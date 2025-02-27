import numpy as np

def submatrix_with_particular_sum(matrix):
    output = []
    dimension = len(matrix)
    for fixed_row in range(dimension):
        for moving_row in range(fixed_row, dimension):
            current_sum = 0
            for fixed_col in range(dimension):
                for moving_col in range(fixed_col, dimension):
                    current_sum += matrix[moving_row][moving_col] - matrix[fixed_row][moving_col] - matrix[moving_row][fixed_col] + matrix[fixed_row][fixed_col]
                    if current_sum == -811:
                        output.append((fixed_row, moving_row, fixed_col, moving_col))
    return output