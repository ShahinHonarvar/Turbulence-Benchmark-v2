import numpy as np

def submatrix_with_particular_sum(matrix):
    matrix_np = np.array(matrix)
    submatrices = []
    for i in range(matrix_np.shape[0]):
        for j in range(matrix_np.shape[1]):
            for x in range(i, matrix_np.shape[0]):
                for y in range(j, matrix_np.shape[1]):
                    submatrix_sum = np.sum(matrix_np[i:x + 1, j:y + 1])
                    if submatrix_sum == 17:
                        submatrix = matrix_np[i:x + 1, j:y + 1]
                        submatrices.append(submatrix.tolist())
    if len(submatrices) == 0:
        return []
    else:
        return submatrices