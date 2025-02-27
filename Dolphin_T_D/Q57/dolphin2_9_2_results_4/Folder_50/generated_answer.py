import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for size1 in range(2, rows - i + 1):
                for size2 in range(2, cols - j + 1):
                    submatrix_sum = np.sum(matrix[i:i + size1, j:j + size2])
                    if submatrix_sum == 95:
                        submatrices.append(matrix[i:i + size1, j:j + size2])
    return submatrices