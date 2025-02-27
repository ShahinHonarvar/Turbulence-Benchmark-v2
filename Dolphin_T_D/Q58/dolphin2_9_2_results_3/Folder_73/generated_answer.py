import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + 1 < len(matrix) and j + 4 < len(matrix[0]):
                if np.all(matrix[i:i + 2, j:j + 5] == 41):
                    count += 1
    return count