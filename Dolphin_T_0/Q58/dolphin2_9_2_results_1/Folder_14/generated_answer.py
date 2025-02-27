import numpy as np

def submatrix_with_n_numbers(matrix):
    sub_matrix_count = 0
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return sub_matrix_count
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            current_count = 0
            for r in range(i, rows):
                for c in range(j, cols):
                    if i == r and j == c:
                        current_count += matrix[i][j]
                    elif i != r and c == j:
                        current_count += matrix[r][j]
                    elif i == r and j != c:
                        current_count += matrix[i][c]
                    elif i != r and j != c:
                        current_count += matrix[r][c]
                    if current_count == 84:
                        sub_matrix_count += 1
    return sub_matrix_count