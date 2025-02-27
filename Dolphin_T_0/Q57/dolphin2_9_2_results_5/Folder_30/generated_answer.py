import numpy

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sub_matrix_sum = numpy.sum(matrix[i:k + 1, j:l + 1])
                    if sub_matrix_sum == 21:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices