import numpy as np

def submatrix_with_n_numbers(matrix, n=176):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(i, matrix.shape[0]):
                for y in range(j, matrix.shape[1]):
                    submatrix = np.array(matrix[i:x + 1, j:y + 1])
                    if len(submatrix.flatten()) == n:
                        count += 1
    return count