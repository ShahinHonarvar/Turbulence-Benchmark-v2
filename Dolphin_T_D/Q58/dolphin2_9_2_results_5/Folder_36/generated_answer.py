import numpy as np

def submatrix_with_n_numbers(matrix):
    size = np.shape(matrix)
    if size[0] < 131 or size[1] < 131:
        return 0
    count = 0
    for i in range(size[0] - 130):
        for j in range(size[1] - 130):
            if np.sum(matrix[i:i + 131, j:j + 131]) == 131 * 131:
                count += 1
    return count