import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            temp_matrix = np.matrix([[matrix[i][j]]])
            for k in range(3):
                for l in range(3):
                    if i + k >= matrix.shape[0] or j + l >= matrix.shape[1]:
                        continue
                    temp_matrix = np.append(temp_matrix, [matrix[i + k][j + l]], axis=0)
            if temp_matrix.shape[0] == 3 and temp_matrix.shape[1] == 3 and np.all(temp_matrix == 60):
                count += 1
    return count