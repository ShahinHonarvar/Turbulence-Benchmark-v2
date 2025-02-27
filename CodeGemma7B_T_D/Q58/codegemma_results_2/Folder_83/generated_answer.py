import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = np.shape(matrix)
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 47:
                for k in range(i, rows):
                    for l in range(j, cols):
                        if np.all(matrix[i:k + 1, j:l + 1] == 47):
                            count += 1
    return count