import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for row_start in range(i + 1):
                for col_start in range(j + 1):
                    for row_end in range(i, len(matrix)):
                        for col_end in range(j, len(matrix[0])):
                            submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                            if np.sum(submatrix) == -65:
                                submatrices.append(submatrix)
    return submatrices