import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for t in range(i + 2, rows + 1):
                for h in range(j + 2, cols + 1):
                    if len(np.array(matrix[i:t, j:h]).flatten()) == 122:
                        count += 1
    return count if count != 0 else 0