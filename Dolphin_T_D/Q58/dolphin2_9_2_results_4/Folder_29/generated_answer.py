import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0
    if matrix.size == 0:
        return 0
    matrix = matrix.tolist()
    height, width = (len(matrix), len(matrix[0]))
    count = 0
    for i in range(height):
        for j in range(width):
            for k in range(i + 1, height):
                for m in range(j + 1, width):
                    if len(set(matrix[i:i + 19][j:j + 19])) == 19 and is_valid(matrix, i, j, k, m):
                        count += 1
    return count

def is_valid(matrix, i, j, k, m):
    height_exp = k - i + 1
    width = m - j + 1
    count_row = len(set([matrix[x][j:m + 1] for x in range(i, k + 1)]))
    count_col = len(set([matrix[i:k + 1][x] for x in range(j, m + 1)]))
    if height_exp * width == 38:
        return count_row == 19 and count_col == 19
    elif height_exp * (width - 1) == 19:
        return count_row == 19
    else:
        return False