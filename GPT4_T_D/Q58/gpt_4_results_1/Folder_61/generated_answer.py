import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = np.shape(matrix)
    if rows < 2 or cols < 2:
        return 0
    else:
        for i in range(rows - 1):
            for j in range(cols - 1):
                submatrix = matrix[i:i + 2, j:j + 2]
                if np.size(submatrix) == 4:
                    count += 1
    return count