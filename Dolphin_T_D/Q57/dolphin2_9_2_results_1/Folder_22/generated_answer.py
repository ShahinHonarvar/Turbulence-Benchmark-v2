import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for size_i in range(i + 1, len(matrix) + 1):
                for size_j in range(j + 1, len(matrix[0]) + 1):
                    subarray = np.array(matrix[i:size_i, j:size_j])
                    if np.sum(subarray) == -38:
                        submatrices.append(subarray)
    return submatrices