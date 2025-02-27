from numpy import *

def submatrix_with_particular_sum(matrix):
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for r in range(row, matrix.shape[0]):
                for c in range(col, matrix.shape[1]):
                    curr_sum = sum(matrix[row:r + 1, col:c + 1])
                    if sum == 862:
                        result.append((row, col, r, c))
    if result != None:
        return result
    else:
        return []