import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 131
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i + int(np.sqrt(n)) <= matrix.shape[0] and j + int(np.sqrt(n)) <= matrix.shape[1]:
                submatrix = matrix[i:int(i + np.sqrt(n)), j:int(j + np.sqrt(n))]
                if submatrix.size == n:
                    count += 1
    return count