import numpy as np

def submatrix_with_particular_sum(matrix):
    final_result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for m in range(i + 1, rows + 1):
                for n in range(j + 1, cols + 1):
                    sub_matrix_sum = np.sum(matrix[i:m, j:n])
                    if sub_matrix_sum == -128:
                        final_result.append(matrix[i:m, j:n])
    return final_result