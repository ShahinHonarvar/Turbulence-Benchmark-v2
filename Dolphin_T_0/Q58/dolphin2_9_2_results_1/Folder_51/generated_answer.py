import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    height, width = matrix.shape
    if height * width < 95:
        return 0
    count = 0
    for i in range(height - 8):
        for j in range(width - 8):
            sub_matrix = matrix[i:i + 9, j:j + 9]
            if np.count_nonzero(sub_matrix == 95) == 9:
                count += 1
    return count