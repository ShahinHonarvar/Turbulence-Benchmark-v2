import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(r1, c1, r2, c2):
        return prefix_sum[r2 + 1][c2 + 1] - prefix_sum[r1][c2 + 1] - prefix_sum[r2 + 1][c1] + prefix_sum[r1][c1]

    def extract_submatrix(r1, c1, r2, c2):
        return matrix[r1:r2 + 1, c1:c2 + 1]
    rows, cols = matrix.shape
    prefix_sum = np.zeros((rows + 1, cols + 1), dtype=int)
    for r in range(rows):
        for c in range(cols):
            prefix_sum[r + 1][c + 1] = matrix[r][c] + prefix_sum[r + 1][c] + prefix_sum[r][c + 1] - prefix_sum[r][c]
    submatrices = []
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    if get_submatrix_sum(r1, c1, r2, c2) == -47:
                        submatrices.append(extract_submatrix(r1, c1, r2, c2))
    return submatrices