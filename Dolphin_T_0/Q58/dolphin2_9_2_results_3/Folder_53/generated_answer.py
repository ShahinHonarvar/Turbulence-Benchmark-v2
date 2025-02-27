import numpy as np

def submatrix_with_n_numbers(mat):
    num_elements = 24
    rows = mat.shape[0]
    cols = mat.shape[1]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == num_elements:
                count += 1
            else:
                for k in range(i + 1, rows):
                    for l in range(j + 1, cols):
                        if set(mat[i:k + 1, j:l + 1].flatten()) == set(range(1, num_elements + 1)):
                            count += 1
    return count