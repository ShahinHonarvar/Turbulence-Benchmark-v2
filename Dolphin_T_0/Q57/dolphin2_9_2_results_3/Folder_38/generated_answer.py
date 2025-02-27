import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    numpy_matrix = np.array(matrix)
    for i in range(numpy_matrix.shape[0]):
        for j in range(numpy_matrix.shape[1]):
            for i2 in range(i, numpy_matrix.shape[0]):
                for j2 in range(j, numpy_matrix.shape[1]):
                    submatrix = numpy_matrix[i:i2 + 1, j:j2 + 1]
                    if submatrix.sum() == 34:
                        submatrices.append(submatrix)
    return submatrices