import numpy as np

def submatrix_with_particular_sum(matrix):
    sum = 0
    ans = []
    for r1 in range(len(matrix)):
        for r2 in range(r1, len(matrix)):
            for c1 in range(len(matrix[0])):
                for c2 in range(c1, len(matrix[0])):
                    sum = 0
                    for r in range(r1, r2 + 1):
                        for c in range(c1, c2 + 1):
                            sum += matrix[r][c]
                    if sum == 77:
                        ans.append([[r1, r2], [c1, c2]])
    return ans