import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    for i in range(rows - 4):
        for j in range(cols - 4):
            sub_matrix = matrix[i:i + 5, j:j + 5]
            if list(sub_matrix.reshape(-1)) == [19] * 25:
                return list(sub_matrix.reshape(-1)).count(19)
    return 0