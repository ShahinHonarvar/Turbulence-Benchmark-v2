import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(input_matrix):
    submatrices = []
    for i in range(len(input_matrix) + 1):
        for j in range(len(input_matrix[0]) + 1):
            for k in combinations(range(len(input_matrix)), i):
                for l in combinations(range(len(input_matrix[0])), j):
                    if len(k) == 0 or len(l) == 0:
                        continue
                    if np.sum(input_matrix[list(k)][list(l)]) == -13:
                        submatrices.append(input_matrix[list(k)][list(l)].tolist())
    return submatrices