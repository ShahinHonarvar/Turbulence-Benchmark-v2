import numpy as np

def submatrix_with_particular_sum(matrix):
    N = len(matrix)
    submatrices = []
    for top in range(N):
        for bottom in range(top, N):
            for left in range(N):
                for right in range(left, N):
                    submatrix_sum = np.sum(matrix[top:bottom + 1, left:right + 1])
                    if submatrix_sum == 8:
                        submatrices.append(matrix[top:bottom + 1, left:right + 1])
    return submatrices