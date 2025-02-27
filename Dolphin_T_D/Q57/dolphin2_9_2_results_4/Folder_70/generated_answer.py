import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    result = []
    length = len(matrix)
    for i in range(length):
        for j in range(length):
            for k in range(i, length):
                for l in range(j, length):
                    submatrix_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if submatrix_sum == 411:
                        result.append(matrix[i:k + 1, j:l + 1].tolist())
    return result