import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    neg = -1 if matrix[0][0] < 0 else 0
    for x1 in range(len(matrix)):
        for y1 in range(len(matrix[0])):
            for x2 in range(x1, len(matrix)):
                for y2 in range(y1, len(matrix[0])):
                    total = 0
                    for i in range(x1, x2 + neg + 1):
                        for j in range(y1, y2 + neg + 1):
                            total += matrix[i][j]
                    if total == 21:
                        result.append([matrix[i][j] for i in range(x1, x2 + neg + 1) for j in range(y1, y2 + neg + 1)])
    return result