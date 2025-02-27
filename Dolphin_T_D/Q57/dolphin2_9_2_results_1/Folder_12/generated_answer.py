import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    matrix_sum = np.sum(matrix)
    if matrix_sum == -83:
        result.append(matrix)
    else:
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                for i_end in range(i, rows):
                    for j_end in range(j, cols):
                        submatrix_sum = np.sum(matrix[i:i_end + 1, j:j_end + 1])
                        if submatrix_sum == -83:
                            result.append(matrix[i:i_end + 1, j:j_end + 1])
    return result