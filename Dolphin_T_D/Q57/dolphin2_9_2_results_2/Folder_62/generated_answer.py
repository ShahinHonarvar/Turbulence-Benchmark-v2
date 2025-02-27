import numpy as np

def submatrix_with_particular_sum(matrix):
    sum = 394
    len_row = len(matrix[0])
    len_col = len(matrix)
    submatrices = []
    for i in range(len_col):
        for j in range(len_row):
            for x in range(i, len_col):
                for y in range(j, len_row):
                    sub_matrix = np.array(matrix[i:x + 1, j:y + 1])
                    if np.sum(sub_matrix) == sum:
                        submatrices.append(sub_matrix)
    if not submatrices:
        return []
    return submatrices