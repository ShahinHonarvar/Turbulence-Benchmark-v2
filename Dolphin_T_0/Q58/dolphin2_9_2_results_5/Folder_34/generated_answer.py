import numpy as np

def submatrix_with_n_numbers(mat):
    submatrix_count = 0
    mat_row, mat_column = mat.shape
    for i in range(mat_row - 2):
        for j in range(mat_column - 2):
            temp = np.array(mat[i:i + 3, j:j + 3])
            if len(temp.flatten()) == 9:
                if (temp == 83).all():
                    submatrix_count += 1
    return submatrix_count