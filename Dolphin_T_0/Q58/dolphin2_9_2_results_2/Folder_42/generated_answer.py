import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    num_elements = np.sum(matrix[i:k + 1, j:l + 1] == 193)
                    if num_elements == 193:
                        count += 1
    return count