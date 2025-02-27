import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for r1 in range(len(matrix)):
        for r2 in range(r1, len(matrix)):
            for c1 in range(len(matrix[0])):
                for c2 in range(c1, len(matrix[0])):
                    if matrix[r1][c1] == matrix[r2][c2] == 144:
                        sub_matrix = matrix[r1:r2 + 1, c1:c2 + 1]
                        if len(sub_matrix) == len(sub_matrix[0]) == np.count_nonzero(sub_matrix == 144):
                            count += 1
    return count