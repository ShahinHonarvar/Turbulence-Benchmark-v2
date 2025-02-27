import numpy as np

def submatrix_with_n_numbers(mat):
    count = 0
    rows, cols = mat.shape
    for i in range(rows):
        for j in range(cols):
            if i < rows - 4 or j < cols - 4 or i > rows - 2 or (j > cols - 2):
                continue
            nums = np.array([mat[i - 2][j - 2], mat[i - 2][j - 1], mat[i - 2][j], mat[i - 1][j - 2], mat[i - 1][j - 1], mat[i - 1][j], mat[i][j - 2], mat[i][j - 1], mat[i][j]])
            if np.all(nums == 53):
                count += 1
    if count == 0:
        return 0
    return count