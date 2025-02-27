import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i + 1, len(matrix)):
                if matrix[i][j] <= 103:
                    continue
                for m in range(j + 1, len(matrix)):
                    if matrix[i][j] <= 103 or matrix[k][m] <= 103:
                        continue
                    for n in range(i + 1, k + 1):
                        for o in range(j + 1, m + 1):
                            if matrix[n][o] <= 103:
                                continue
                            count += 1
    return count