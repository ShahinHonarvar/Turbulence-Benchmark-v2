import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    found_submatrices = []
    for r1 in range(rows):
        for r2 in range(r1, rows):
            temp = np.zeros(cols, dtype=int)
            for c in range(cols):
                for r in range(r1, r2 + 1):
                    temp[c] += matrix[r][c]
            for start in range(cols):
                curr_sum = 0
                for end in range(start, cols):
                    curr_sum += temp[end]
                    if curr_sum == 93:
                        submatrix = matrix[r1:r2 + 1, start:end + 1].tolist()
                        found_submatrices.append(submatrix)
    return found_submatrices