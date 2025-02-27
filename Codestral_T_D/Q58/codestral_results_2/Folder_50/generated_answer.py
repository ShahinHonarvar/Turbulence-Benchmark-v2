import numpy as np

def submatrix_with_n_numbers(matrix, n=40):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - int(np.sqrt(n)) + 1):
        for j in range(cols - int(np.sqrt(n)) + 1):
            for k in range(i + int(np.sqrt(n)), rows + 1):
                for l in range(j + int(np.sqrt(n)), cols + 1):
                    if np.size(matrix[i:k, j:l]) == n:
                        count += 1
    return count