import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height, width = matrix.shape
    for i in range(height - 1, -1, -1):
        for j in range(width - 1, -1, -1):
            submatrix = matrix[i:height, j:width]
            if np.all(submatrix == 77):
                count += 1
    return count