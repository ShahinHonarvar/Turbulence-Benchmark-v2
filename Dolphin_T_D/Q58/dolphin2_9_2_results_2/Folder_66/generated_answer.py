import numpy as np

def submatrix_with_n_numbers(matrix):
    size = np.shape(matrix)
    count = 0
    for i in range(size[0]):
        for j in range(size[1]):
            if i <= size[0] - 6 and j <= size[1] - 6:
                submatrix = matrix[i:i + 6, j:j + 6]
                if 42 in submatrix:
                    count += 1
    return count