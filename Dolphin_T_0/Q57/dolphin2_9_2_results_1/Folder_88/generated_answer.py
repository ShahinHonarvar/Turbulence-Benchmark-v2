import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for a in range(i, len(matrix)):
                for b in range(j, len(matrix[i])):
                    sub_matrix = np.array(matrix[i:a + 1, j:b + 1])
                    if np.sum(sub_matrix) == -64:
                        submatrices.append(sub_matrix)
    return submatrices