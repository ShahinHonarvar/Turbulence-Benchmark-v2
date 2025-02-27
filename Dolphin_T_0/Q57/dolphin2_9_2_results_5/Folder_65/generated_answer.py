import numpy as np

def submatrix_with_particular_sum(matrix):
    i, j, n, m = (0, 0, len(matrix), len(matrix[0]))
    result = []
    while i < n:
        while j < m:
            for k in range(i, n):
                for l in range(j, m):
                    restromatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(restromatrix) == 78:
                        result.append(restromatrix)
            j += 1
        j = 0
        i += 1
    if len(result) == 0:
        return []
    return result