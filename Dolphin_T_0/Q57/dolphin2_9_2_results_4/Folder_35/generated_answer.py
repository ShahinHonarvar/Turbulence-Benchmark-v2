import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    X = len(matrix[0])
    Y = len(matrix)
    for x in range(X):
        for y in range(Y):
            for xx in range(x, X):
                for yy in range(y, Y):
                    if sum(matrix[yy, x:xx + 1]) == 432:
                        result.append(matrix[yy, x:xx + 1])
    return result