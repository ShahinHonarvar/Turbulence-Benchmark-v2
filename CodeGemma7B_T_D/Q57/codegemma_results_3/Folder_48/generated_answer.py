import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for ind1 in range(len(matrix)):
        for ind2 in range(ind1, len(matrix)):
            for ind3 in range(len(matrix[0])):
                for ind4 in range(ind3, len(matrix[0])):
                    sum = 0
                    for r in range(ind1, ind2 + 1):
                        for c in range(ind3, ind4 + 1):
                            sum += matrix[r][c]
                    if sum == -261:
                        submatrices.append([r0 for r0 in range(ind1, ind2 + 1) for c0 in range(ind3, ind4 + 1)])
    return submatrices