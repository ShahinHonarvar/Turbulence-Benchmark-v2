import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, r1, c1, r2, c2):
        return mat[r2 + 1, c2 + 1] - mat[r2 + 1, c1] - mat[r1, c2 + 1] + mat[r1, c1]
    rows, cols = matrix.shape
    integral_image = np.zeros((rows + 1, cols + 1), dtype=int)
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            integral_image[r, c] = matrix[r - 1, c - 1] + integral_image[r - 1, c] + integral_image[r, c - 1] - integral_image[r - 1, c - 1]
    results = []
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    if submatrix_sum(integral_image, r1, c1, r2, c2) == 245:
                        submatrix = matrix[r1:r2 + 1, c1:c2 + 1].copy()
                        results.append(submatrix)
    return results