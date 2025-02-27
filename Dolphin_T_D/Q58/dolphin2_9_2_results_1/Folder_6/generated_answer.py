import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_counts = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = np.array(matrix[i:k + 1, j:l + 1])
                    if len(submatrix) * len(submatrix[0]) == 122:
                        matrix_counts += 1
    return matrix_counts