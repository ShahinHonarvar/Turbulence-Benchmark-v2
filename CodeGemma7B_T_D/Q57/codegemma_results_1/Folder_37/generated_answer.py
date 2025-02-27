import numpy as np

def submatrix_with_particular_sum(matrix):
    Result_list = []
    for i in range(matrix.shape[0]):
        for j in range(i, matrix.shape[0]):
            for k in range(matrix.shape[1]):
                for l in range(k, matrix.shape[1]):
                    Sum_abcd = sum(matrix[i:j + 1, k:l + 1].flatten())
                    if Sum_abcd == -82:
                        Result_list.append(matrix[i:j + 1, k:l + 1])
    return Result_list