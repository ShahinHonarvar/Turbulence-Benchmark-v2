import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i + 2 < matrix.shape[0] and j + 2 < matrix.shape[1]:
                submatrix = matrix[i:i + 3, j:j + 3]
                if submatrix.all() or np.fliplr(submatrix).all() or np.flipud(submatrix).all() or np.rot90(submatrix).all():
                    if submatrix.sum() == 111:
                        count += 1
    return count