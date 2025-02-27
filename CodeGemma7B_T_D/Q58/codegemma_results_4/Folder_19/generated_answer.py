import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for r in range(i + 1):
                for c in range(j + 1):
                    submatrix = matrix[r:i + 1, c:j + 1]
                    if np.unique(submatrix).size == 17:
                        count += 1
    return count