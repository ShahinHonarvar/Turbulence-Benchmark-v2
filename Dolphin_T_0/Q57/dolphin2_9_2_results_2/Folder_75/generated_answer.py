import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    length = len(matrix)
    for i in range(length):
        for j in range(length):
            for start_row in range(i, length + 1):
                for end_row in range(start_row, length + 1):
                    for start_col in range(j, length + 1):
                        for end_col in range(start_col, length + 1):
                            submatrix_sum = np.sum(matrix[start_row:end_row, start_col:end_col])
                            if submatrix_sum == 16:
                                submatrices.append(matrix[start_row:end_row, start_col:end_col])
    return submatrices