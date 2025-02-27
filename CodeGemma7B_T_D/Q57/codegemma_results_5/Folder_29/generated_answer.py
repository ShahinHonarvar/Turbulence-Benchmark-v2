import numpy as np

def submatrix_with_particular_sum(matrix):
    list_result = []
    for x in range(len(matrix)):
        for y in range(x, len(matrix)):
            for z in range(x, y + 1):
                for w in range(z, y + 1):
                    sum_possible = 0
                    list_current = []
                    for m in range(z, w + 1):
                        for n in range(x, y + 1):
                            sum_possible += matrix[m][n]
                            list_current.append(matrix[m][n])
                    if sum_possible == 84:
                        list_result.append(list_current)
    if not list_result:
        list_result.append([])
    return list_result