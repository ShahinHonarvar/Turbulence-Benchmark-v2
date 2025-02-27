import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for row_index_1 in range(len(matrix)):
        for row_index_2 in range(row_index_1, len(matrix)):
            for col_index_1 in range(len(matrix[0])):
                for col_index_2 in range(col_index_1, len(matrix[0])):
                    submatrix = matrix[row_index_1:row_index_2 + 1, col_index_1:col_index_2 + 1]
                    if np.sum(submatrix) == 1:
                        result.append(submatrix)
    return result