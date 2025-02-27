import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 1:
                if i > 0 and matrix[i - 1][j] == 0 or i == 0:
                    if j > 0 and matrix[i][j - 1] == 0 or j == 0:
                        for x in range(i, height):
                            for y in range(j, width):
                                if matrix[x][y] == 1:
                                    if x == y:
                                        sub_matrix = matrix[i:x + 1, j:y + 1]
                                        if np.count_nonzero(sub_matrix) == 51:
                                            count += 1
    return count