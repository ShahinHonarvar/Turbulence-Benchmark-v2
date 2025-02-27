import numpy as np

def submatrix_with_particular_sum(matrix):
    sub_lists = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for n in range(j, len(matrix[0])):
                    if np.sum(matrix[i:k + 1, j:n + 1]) == 56:
                        sub_lists.append(matrix[i:k + 1, j:n + 1])
    if not sub_lists:
        return []
    else:
        return sub_lists