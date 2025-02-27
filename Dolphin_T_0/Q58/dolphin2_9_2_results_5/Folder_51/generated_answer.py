import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    loop_matrix = np.array(matrix)
    for i in range(loop_matrix.shape[0]):
        for j in range(loop_matrix.shape[1]):
            if loop_matrix[i][j] == 95:
                if (loop_matrix[i - 1:i + 2, j - 1:j + 2] == 95).all():
                    count += 1
    return count