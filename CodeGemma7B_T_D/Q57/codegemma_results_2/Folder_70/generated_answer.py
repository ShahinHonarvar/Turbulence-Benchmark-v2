import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_411 = 0
    for row in matrix:
        for col in range(len(row)):
            for r in range(row, len(matrix)):
                for c in range(col, len(row)):
                    submatrix = matrix[row:r + 1, col:c + 1]
                    if np.sum(submatrix) == 411:
                        sum_411 += 1
    return sum_411