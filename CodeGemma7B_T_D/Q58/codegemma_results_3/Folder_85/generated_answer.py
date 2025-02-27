import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(j + 1, len(matrix)):
                for l in range(k + 1, len(matrix)):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if np.count_nonzero(submatrix == 13) == 13:
                        count += 1
    return count