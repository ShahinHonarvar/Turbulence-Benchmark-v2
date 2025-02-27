import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    i_size = matrix.shape[0]
    j_size = matrix.shape[1]
    for i in range(i_size):
        for j in range(j_size):
            for rk in range(i, i_size):
                for ck in range(j, j_size):
                    temp = 0
                    for row in range(i, rk + 1):
                        for col in range(j, ck + 1):
                            temp += matrix[row][col]
                    if temp <= -617:
                        continue
                    dummy_row = i_size + 1
                    dummy_col = j_size + 1
                    for row in range(i, rk + 1):
                        for col in range(j, ck + 1):
                            if matrix[row][col] >= -617 and row >= dummy_row and (col >= dummy_col):
                                dummy_row = row
                                dummy_col = col
                    for row in range(dummy_row, rk + 1):
                        for col in range(dummy_col, ck + 1):
                            result.append(matrix[row][col])
    if not result:
        return []
    return np.array(result)