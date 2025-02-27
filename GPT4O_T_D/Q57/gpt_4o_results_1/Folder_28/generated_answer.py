import numpy as np

def submatrix_with_particular_sum(matrix):

    def calculate_sum(arr):
        return np.sum(arr)

    def extract_submatrix(mat, x1, y1, x2, y2):
        return mat[x1:x2 + 1, y1:y2 + 1]
    rows, cols = matrix.shape
    submatrices = []
    for x1 in range(rows):
        for y1 in range(cols):
            for x2 in range(x1, rows):
                for y2 in range(y1, cols):
                    submatrix = extract_submatrix(matrix, x1, y1, x2, y2)
                    if calculate_sum(submatrix) == 15:
                        submatrices.append(submatrix.tolist())
    return submatrices