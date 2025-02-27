import numpy as np

def submatrix_with_n_numbers(matrix):
    s = np.shape(matrix)
    total = 0
    for i in range(s[0]):
        for j in range(s[1]):
            if i + 3 < s[0] and j + 3 < s[1]:
                total += np.all(matrix[i:i + 4, j:j + 4] == 45)
    return total