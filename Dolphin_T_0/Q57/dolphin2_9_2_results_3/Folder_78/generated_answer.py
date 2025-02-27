import numpy as np

def submatrix_with_particular_sum(matrix):
    sums = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for row in range(i, len(matrix)):
                for col in range(j, len(matrix[0])):
                    submatrix = matrix[i:row + 1, j:col + 1]
                    if np.sum(submatrix) == 17:
                        sums.append(submatrix)
    return sums