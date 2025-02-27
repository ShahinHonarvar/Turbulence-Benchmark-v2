import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for r1 in range(rows):
        for r2 in range(r1, rows):
            row_sum = np.zeros(cols)
            for c in range(cols):
                for r in range(r1, r2 + 1):
                    row_sum[c] += matrix[r][c]
            for c1 in range(cols):
                current_sum = 0
                for c2 in range(c1, cols):
                    current_sum += row_sum[c2]
                    if current_sum == 80:
                        submatrix = matrix[r1:r2 + 1, c1:c2 + 1].tolist()
                        result.append(submatrix)
    return result