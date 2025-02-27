import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    n, m = matrix.shape
    for top in range(n):
        for left in range(m):
            for bottom in range(top, n):
                for right in range(left, m):
                    submatrix = matrix[top:bottom + 1, left:right + 1].sum()
                    if submatrix == -43:
                        result.append(matrix[top:bottom + 1, left:right + 1])
    return result