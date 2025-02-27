import numpy as np

def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    num_rows, num_cols = matrix.shape
    submatrices = []
    for i in range(num_rows - 1):
        for j in range(num_cols - 1):
            for i_end in range(i + 1, num_rows):
                for j_end in range(j + 1, num_cols):
                    submatrix = matrix[i:i_end + 1, j:j_end + 1]
                    submatrix_sum = np.sum(submatrix)
                    if submatrix_sum == 901:
                        submatrices.append(submatrix)
    if len(submatrices) == 0:
        return []
    else:
        return submatrices