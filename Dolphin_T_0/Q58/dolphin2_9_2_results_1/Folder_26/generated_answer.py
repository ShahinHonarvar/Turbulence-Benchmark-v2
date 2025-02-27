import numpy

def submatrix_with_n_numbers(matrix):
    submatrices = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(i, matrix.shape[0]):
                for y in range(j, matrix.shape[1]):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if submatrix.size == 115:
                        submatrices += 1
    return submatrices