import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for r1 in range(rows):
        for r2 in range(r1, rows):
            cumulative = np.zeros(cols)
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    sub_sum = 0
                    for i in range(r1, r2 + 1):
                        for j in range(c1, c2 + 1):
                            sub_sum += matrix[i][j]
                    if sub_sum == 862:
                        submatrix = [matrix[i][c1:c2 + 1] for i in range(r1, r2 + 1)]
                        result.append(submatrix)
    return result