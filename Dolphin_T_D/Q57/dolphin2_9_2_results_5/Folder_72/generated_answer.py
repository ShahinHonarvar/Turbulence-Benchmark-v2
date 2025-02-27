import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    row_count, column_count = matrix.shape
    for i in range(row_count):
        for j in range(column_count):
            for x in range(i, row_count):
                for y in range(j, column_count):
                    current_submatrix = matrix[i:x + 1, j:y + 1]
                    if current_submatrix.sum() == 41:
                        submatrices.append(current_submatrix)
    return submatrices