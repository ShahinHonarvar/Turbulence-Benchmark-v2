import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix_sum = np.sum(matrix)
    for top in range(matrix.shape[0]):
        for left in range(matrix.shape[1]):
            for bottom in range(top, matrix.shape[0]):
                for right in range(left, matrix.shape[1]):
                    submatrix_sum = np.sum(matrix[top:bottom + 1, left:right + 1])
                    if submatrix_sum == 100:
                        submatrices.append(matrix[top:bottom + 1, left:right + 1])
    return submatrices