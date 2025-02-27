import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for x in range(i, len(matrix)):
                for y in range(j, len(matrix[0])):
                    sub_matrix = np.array(matrix[i:x + 1, j:y + 1])
                    if np.sum(sub_matrix) == 80:
                        submatrices.append(sub_matrix)
    return submatrices