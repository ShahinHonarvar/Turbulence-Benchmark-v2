import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for x in range(i, len(matrix)):
                for y in range(j, len(matrix[0])):
                    s = np.sum(matrix[i:x + 1, j:y + 1])
                    if s == 17:
                        row_slice = matrix[i:x + 1, :]
                        col_slice = row_slice[:, j:y + 1]
                        result.append(col_slice)
    return result