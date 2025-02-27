import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                continue
            new_matrix = np.zeros((3, 3))
            for k in range(3):
                for l in range(3):
                    if i - 1 + k >= 0 and i - 1 + k < len(matrix) and (j - 1 + l >= 0) and (j - 1 + l < len(matrix[0])):
                        new_matrix[k][l] = matrix[i - 1 + k][j - 1 + l]
            if np.size(np.where(new_matrix == 131)) == 131:
                count += 1
    return count