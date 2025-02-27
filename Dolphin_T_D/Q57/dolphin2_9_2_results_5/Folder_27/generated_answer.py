import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_submatrixes = []
    M, N = (len(matrix), len(matrix[0]))
    for sum_m in range(1, min(M, N) + 1):
        for sum_n in range(1, min(M, N) + 1):
            for i in range(M - sum_m + 1):
                for j in range(N - sum_n + 1):
                    if np.sum(matrix[i:i + sum_m, j:j + sum_n]) == 77:
                        sum_submatrixes.append(matrix[i:i + sum_m, j:j + sum_n])
    return sum_submatrixes