import numpy as np

def submatrix_with_n_numbers(matrix):
    hshape = matrix.shape[0]
    vshape = matrix.shape[1]
    count = 0
    for i in range(hshape):
        for j in range(vshape):
            if i + 4 < hshape and j + 4 < vshape:
                if np.all(matrix[i:i + 4, j:j + 4] == 24):
                    count += 1
    return count