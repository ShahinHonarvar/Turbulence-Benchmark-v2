import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - int(np.sqrt(57)) + 1):
        for j in range(cols - int(np.sqrt(57)) + 1):
            submatrix = matrix[i:i + int(np.sqrt(57)), j:j + int(np.sqrt(57))]
            if submatrix.size == 57:
                count += 1
    return count