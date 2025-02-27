import numpy as np

def submatrix_with_particular_sum(matrix):
    sub_matrices = []
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            for k in range(i + 1, height):
                for l in range(j + 1, width):
                    num_matrix = np.array(matrix[i:k, j:l])
                    if num_matrix.sum() == 34:
                        sub_matrices.append(num_matrix.tolist())
    if not sub_matrices:
        return []
    else:
        return sub_matrices