import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k + 1, len(matrix[0])):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if submatrix.sum() == 432:
                        result.append(submatrix)
    if result:
        return result
    else:
        return []