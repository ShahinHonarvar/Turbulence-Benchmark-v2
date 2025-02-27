import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_to_find = 830
    N = len(matrix)
    result = []
    for x in range(N):
        for y in range(N):
            for p in range(x + 1, N + 1):
                for q in range(y + 1, N + 1):
                    submatrix_sum = np.sum(matrix[x:p, y:q])
                    if submatrix_sum == sum_to_find:
                        result.append(matrix[x:p, y:q])
    return result