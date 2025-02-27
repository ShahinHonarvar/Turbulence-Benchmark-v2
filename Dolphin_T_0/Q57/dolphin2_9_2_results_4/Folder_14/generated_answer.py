import numpy as np

def submatrix_with_particular_sum(matrix):
    list_of_sub_matrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = np.array(matrix[i:k + 1, j:l + 1])
                    if sum(submatrix.flatten()) == -93:
                        list_of_sub_matrices.append(submatrix)
    return list_of_sub_matrices