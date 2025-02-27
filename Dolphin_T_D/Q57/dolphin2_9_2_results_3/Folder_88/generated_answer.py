import numpy as np

def submatrix_with_particular_sum(matrix):
    list_of_submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for r in range(i, len(matrix)):
                for c in range(j, len(matrix[0])):
                    submatrix = np.array(matrix[i:r + 1, j:c + 1])
                    if np.sum(submatrix) == -64 and submatrix.size != 0:
                        list_of_submatrices.append(submatrix)
    return list_of_submatrices