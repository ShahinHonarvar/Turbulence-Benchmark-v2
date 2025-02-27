from numpy import *

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    temp_sum = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            temp_sum += matrix[m][n]
                    if temp_sum == -64:
                        result.append([[i, j], [k, l]])
    return result