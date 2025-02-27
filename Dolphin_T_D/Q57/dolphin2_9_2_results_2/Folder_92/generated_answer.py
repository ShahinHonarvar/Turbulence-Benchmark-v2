import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return submatrices
    height, width = matrix.shape
    sum_ - 3
    for h in range(height):
        for w in range(width):
            for hh in range(h, height):
                for ww in range(w, width):
                    submatrix_sum = np.sum(matrix[h:hh + 1, w:ww + 1])
                    if submatrix_sum == sum_:
                        submatrices.append(matrix[h:hh + 1, w:ww + 1])
    return submatrices