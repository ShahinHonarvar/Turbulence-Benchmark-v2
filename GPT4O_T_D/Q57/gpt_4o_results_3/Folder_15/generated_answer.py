import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices_of_size(r, c, height, width):
        submatrices = []
        for i in range(r - height + 1):
            for j in range(c - width + 1):
                submatrices.append(matrix[i:i + height, j:j + width])
        return submatrices
    rows, cols = matrix.shape
    res = []
    for height in range(1, rows + 1):
        for width in range(1, cols + 1):
            submatrices = get_submatrices_of_size(rows, cols, height, width)
            for submatrix in submatrices:
                if np.sum(submatrix) == -9:
                    res.append(submatrix.tolist())
    return res