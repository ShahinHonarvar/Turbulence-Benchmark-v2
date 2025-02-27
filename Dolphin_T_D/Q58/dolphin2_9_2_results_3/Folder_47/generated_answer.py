import numpy as np

def submatrix_with_n_numbers(mat):
    rows, cols = mat.shape
    counter = 0
    for i in range(rows):
        for j in range(cols):
            for i2 in range(i + 1, rows):
                for j2 in range(j + 1, cols):
                    if len(np.array(mat[i:i2, j:j2])) == 90:
                        counter += 1
    return counter