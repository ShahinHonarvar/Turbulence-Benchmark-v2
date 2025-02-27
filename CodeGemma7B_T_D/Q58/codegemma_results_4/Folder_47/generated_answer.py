import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    for i in range(row):
        for j in range(col):
            for k in range(i + 1, row):
                for l in range(j + 1, col):
                    temp_matrix = matrix[i:k + 1, j:l + 1]
                    if np.unique(temp_matrix).size == 90 and np.unique(temp_matrix).size == temp_matrix.size:
                        count += 1
    return count