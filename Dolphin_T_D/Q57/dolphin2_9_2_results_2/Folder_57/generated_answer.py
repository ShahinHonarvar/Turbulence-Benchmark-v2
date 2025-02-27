import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    matrix = np.array(matrix)
    matrix = matrix.tolist()
    row_num = len(matrix)
    col_num = len(matrix[0])
    for r1 in range(row_num):
        for r2 in range(r1, row_num):
            for c1 in range(col_num):
                for c2 in range(c1, col_num):
                    if (r2 - r1 + 1) * (c2 - c1 + 1) != 13:
                        continue
                    submatrix = [map(int, row) for row in matrix[r1:r2 + 1]]
                    if np.numpy.sum(submatrix) == 13:
                        result.append(submatrix)
    return result