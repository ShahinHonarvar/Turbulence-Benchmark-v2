import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    row, col = matrix.shape
    for i in range(row):
        for j in range(col):
            for i_end in range(i, row):
                for j_end in range(j, col):
                    submatrix = np.array(matrix[i:i_end + 1, j:j_end + 1]).sum()
                    if submatrix == 15:
                        submatrices.append(matrix[i:i_end + 1, j:j_end + 1].tolist())
    return submatrices