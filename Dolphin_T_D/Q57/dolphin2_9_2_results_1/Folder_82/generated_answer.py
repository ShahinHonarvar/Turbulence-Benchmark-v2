import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    if isinstance(matrix, np.ndarray):
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                for i_end in range(i, matrix.shape[0]):
                    for j_end in range(j, matrix.shape[1]):
                        submatrix = matrix[i:i_end + 1, j:j_end + 1]
                        if np.sum(submatrix) == -27:
                            submatrices.append(submatrix.tolist())
    return submatrices