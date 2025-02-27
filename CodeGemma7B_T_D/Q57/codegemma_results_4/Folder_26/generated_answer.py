import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for h in range(i + 1, len(matrix)):
                for k in range(j + 1, len(matrix[0])):
                    sum = 0
                    for p in range(i, h + 1):
                        for q in range(j, k + 1):
                            sum += matrix[p][q]
                    if sum == 997:
                        result.append([matrix[p][q] for p in range(i, h + 1) for q in range(j, k + 1)])
    return result