import numpy as np

def submatrix_with_particular_sum(matrix):
    final_result = []
    row_of_matrix = len(matrix)
    column_of_matrix = len(matrix[0])
    for i in range(row_of_matrix):
        for j in range(column_of_matrix):
            for k in range(i + 1, row_of_matrix + 1):
                for l in range(j + 1, column_of_matrix + 1):
                    matrix_piece = matrix[i:k, j:l]
                    if np.sum(matrix_piece) == -81:
                        final_result.append(matrix_piece)
    return final_result