import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(1, len(matrix) + 1):
        for pair in combinations(range(len(matrix[0])), 2):
            top = min(pair)
            bottom = max(pair)
            for j in range(i, len(matrix) + 1):
                submatrix = np.array(matrix[top:bottom + 1, j - i:j])
                if np.sum(submatrix) == 27:
                    result.append(submatrix)
    return result