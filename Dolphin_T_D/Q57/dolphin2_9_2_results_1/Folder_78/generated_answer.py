import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for top in range(0, len(matrix)):
        for left in range(0, len(matrix[0])):
            for bottom in range(top, len(matrix)):
                for right in range(left, len(matrix[0])):
                    if sum((sum((matrix[i][j] for j in range(left, right + 1))) for i in range(top, bottom + 1))) == 17:
                        submatrices.append(matrix[top:bottom + 1, left:right + 1].tolist())
    return submatrices