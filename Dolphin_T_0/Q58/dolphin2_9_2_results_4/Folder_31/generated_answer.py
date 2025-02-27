import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i <= len(matrix) - 3 and j <= len(matrix[0]) - 3:
                if np.all(matrix[i:i + 3, j:j + 3] == 45):
                    count += 1
    return count