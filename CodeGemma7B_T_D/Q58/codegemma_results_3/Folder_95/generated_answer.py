import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] == 87:
                for k in range(i, matrix.shape[0]):
                    for l in range(j, matrix.shape[1]):
                        if np.all(matrix[i:k + 1, j:l + 1] == 87):
                            count += 1
    return count