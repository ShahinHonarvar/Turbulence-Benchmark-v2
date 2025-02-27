import numpy as np

def submatrix_with_particular_sum(matrix):
    list_of_sub_matrix = []
    for i in range(matrix.shape[0] + 1):
        for j in range(matrix.shape[1] + 1):
            for k in range(i):
                for l in range(j):
                    sum = 0
                    for m in range(i - k):
                        for n in range(j - l):
                            sum += matrix[k + m][l + n]
                    if sum == 126:
                        list_of_sub_matrix.append(matrix[k:i, l:j])
    if len(list_of_sub_matrix) == 0:
        return []
    return list_of_sub_matrix