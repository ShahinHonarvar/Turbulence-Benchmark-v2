import numpy as np

def submatrix_with_particular_sum(matrix):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                for l in range(len(matrix)):
                    if i <= k and l <= j:
                        sub_matrix = matrix[i:k + 1, j:l + 1]
                        sum_of_elements = sub_matrix.sum()
                        if sum_of_elements == -13:
                            res.append(sub_matrix)
    return res