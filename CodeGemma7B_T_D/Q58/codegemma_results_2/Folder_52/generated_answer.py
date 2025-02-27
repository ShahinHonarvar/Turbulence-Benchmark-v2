import numpy as np

def submatrix_with_n_numbers(matrix):
    ans = 0
    for r1 in range(matrix.shape[0]):
        for r2 in range(r1 + 1, matrix.shape[0] + 1):
            temp = set()
            for c1 in range(matrix.shape[1]):
                for c2 in range(c1 + 1, matrix.shape[1] + 1):
                    if matrix[r1:r2, c1:c2] in temp:
                        ans += 1
                        break
                    temp.add(matrix[r1:r2, c1:c2])
    return ans