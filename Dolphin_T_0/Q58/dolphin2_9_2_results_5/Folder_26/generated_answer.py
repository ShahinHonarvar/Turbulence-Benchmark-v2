import numpy as np

def submatrix_with_n_numbers(matrix):
    n_count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if x + 3 < len(matrix) and y + 3 < len(matrix[0]):
                submatrix = np.array([[matrix[x][y], matrix[x + 1][y], matrix[x][y + 1], matrix[x + 1][y + 1]], [matrix[x + 2][y], matrix[x + 3][y], matrix[x + 2][y + 1], matrix[x + 3][y + 1]], [matrix[x][y + 2], matrix[x + 1][y + 2], matrix[x][y + 3], matrix[x + 1][y + 3]], [matrix[x + 2][y + 2], matrix[x + 3][y + 2], matrix[x + 2][y + 3], matrix[x + 3][y + 3]]])
                if np.sum(submatrix) == 115:
                    n_count += 1
    return n_count