import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if len(matrix[i:i + 5]) >= 5 and len(matrix[i:i + 5][0]) >= 5:
                if np.sum(matrix[i:i + 5, j:j + 5]) == 130:
                    count += 1
    return count