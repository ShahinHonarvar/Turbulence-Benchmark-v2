import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 66
    count = 0
    for i_row in range(len(matrix)):
        for j_col in range(len(matrix[0])):
            for i_end in range(i_row, len(matrix)):
                for j_end in range(j_col, len(matrix[0])):
                    count += 1 if (i_end - i_row + 1) * (j_end - j_col + 1) == n else 0
    return count