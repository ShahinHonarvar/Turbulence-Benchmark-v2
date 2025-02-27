import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(top_left, bottom_right, prefix_sum):
        x1, y1 = top_left
        x2, y2 = bottom_right
        total = prefix_sum[x2 + 1][y2 + 1]
        if x1 > 0:
            total -= prefix_sum[x1][y2 + 1]
        if y1 > 0:
            total -= prefix_sum[x2 + 1][y1]
        if x1 > 0 and y1 > 0:
            total += prefix_sum[x1][y1]
        return total
    rows, cols = matrix.shape
    prefix_sum = np.zeros((rows + 1, cols + 1), dtype=int)
    for i in range(rows):
        for j in range(cols):
            prefix_sum[i + 1][j + 1] = matrix[i][j] + prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j]
    submatrices = []
    for x1 in range(rows):
        for y1 in range(cols):
            for x2 in range(x1, rows):
                for y2 in range(y1, cols):
                    if get_submatrix_sum((x1, y1), (x2, y2), prefix_sum) == -13:
                        submatrices.append(matrix[x1:x2 + 1, y1:y2 + 1].copy())
    return submatrices