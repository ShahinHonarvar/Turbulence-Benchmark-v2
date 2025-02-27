import numpy

def submatrix_with_n_numbers(matrix):
    matrix = numpy.array(matrix)
    count = 0
    for i1 in range(matrix.shape[0]):
        for i2 in range(i1 + 1, matrix.shape[0]):
            for j1 in range(matrix.shape[1]):
                for j2 in range(j1 + 1, matrix.shape[1]):
                    submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
                    if numpy.count_nonzero(submatrix == 175) == 175:
                        count += 1
    return count