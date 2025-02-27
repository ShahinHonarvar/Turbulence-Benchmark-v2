from numpy import asarray, matmul
        import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_list = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix) + 1):
            for k in range(len(matrix[0])):
                for l in range(k + 1, len(matrix[0]) + 1):
                    submatrix = matrix[i:j, k:l]
                    if sum(submatrix.flatten()) == -811:
                        sum_list.append(submatrix)
    return sum_list