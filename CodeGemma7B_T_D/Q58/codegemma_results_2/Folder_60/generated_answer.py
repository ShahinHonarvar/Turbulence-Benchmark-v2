import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for m in range(i, len(matrix)):
                for n in range(j, len(matrix[0])):
                    submatrix = matrix[i:m + 1, j:n + 1]
                    if np.count_nonzero(submatrix == 88) == 88:
                        count += 1
    return count