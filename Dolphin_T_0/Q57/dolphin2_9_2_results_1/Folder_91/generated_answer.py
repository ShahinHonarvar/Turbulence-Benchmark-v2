import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    submatrix_list = []
    size = len(matrix)
    for i in range(size):
        for j in range(i + 1, size):
            for k in range(size):
                for l in range(k + 1, size):
                    submatrix = matrix[i:j, k:l]
                    submatrix_sum = np.sum(submatrix)
                    if submatrix_sum == -6:
                        submatrix_list.append(submatrix.tolist())
    return submatrix_list