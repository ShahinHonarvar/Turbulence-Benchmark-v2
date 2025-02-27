import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, required_sum):
        submatrices = []
        for r in range(matrix.shape[0]):
            for c in range(matrix.shape[1]):
                if r + 1 < matrix.shape[0] and c + 1 < matrix.shape[1]:
                    temp_matrix = matrix[r:r + 2, c:c + 2]
                    if np.sum(temp_matrix) == required_sum:
                        submatrices.append(temp_matrix)
        return submatrices
    required_sum = 94
    submatrices = find_submatrices(matrix, required_sum)
    if not submatrices:
        return []
    else:
        return submatrices