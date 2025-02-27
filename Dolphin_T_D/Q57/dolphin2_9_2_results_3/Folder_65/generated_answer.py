import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    x, y = matrix.shape
    for i in range(x):
        for j in range(y):
            for z in range(i + 1, x + 1):
                for w in range(j + 1, y + 1):
                    if sum(matrix[i:z, j:w]) == 78:
                        results.append(matrix[i:z, j:w])
    if not results:
        return []
    return results