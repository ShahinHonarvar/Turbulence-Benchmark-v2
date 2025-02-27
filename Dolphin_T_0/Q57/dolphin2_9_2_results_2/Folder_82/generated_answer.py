import numpy

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rlen, clen = matrix.shape
    for i in range(rlen):
        for j in range(clen):
            for k in range(i, rlen):
                for l in range(j, clen):
                    if numpy.sum(matrix[i:k + 1, j:l + 1]) == -27:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices