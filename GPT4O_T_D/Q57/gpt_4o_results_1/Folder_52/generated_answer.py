import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(prefix_sum, target_sum):
        submatrices = []
        rows, cols = (len(prefix_sum) - 1, len(prefix_sum[0]) - 1)
        for r1 in range(1, rows + 1):
            for r2 in range(r1, rows + 1):
                for c1 in range(1, cols + 1):
                    for c2 in range(c1, cols + 1):
                        total = prefix_sum[r2][c2] - prefix_sum[r1 - 1][c2] - prefix_sum[r2][c1 - 1] + prefix_sum[r1 - 1][c1 - 1]
                        if total == target_sum:
                            submatrix = [matrix[i - 1][c1 - 1:c2] for i in range(r1, r2 + 1)]
                            submatrices.append(submatrix)
        return submatrices
    rows, cols = matrix.shape
    prefix_sum = np.zeros((rows + 1, cols + 1), dtype=int)
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
    return find_submatrices_with_sum(prefix_sum, 100)