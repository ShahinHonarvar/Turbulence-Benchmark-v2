import numpy as np

def submatrix_with_particular_sum(matrix):
    sums, submatrices = ([], [])
    n, m = matrix.shape
    for top in range(n):
        for left in range(m):
            for bottom in range(top + 1, n + 1):
                for right in range(left + 1, m + 1):
                    submatrix = matrix[top:bottom, left:right].sum()
                    if submatrix == 13:
                        submatrices.append(matrix[top:bottom, left:right])
    return submatrices if submatrices else []