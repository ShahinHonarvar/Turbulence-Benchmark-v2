import numpy

def submatrix_with_particular_sum(matrix):
    h, w = matrix.shape
    submatrices = []
    for i in range(h):
        for j in range(w):
            for x in range(i + 1, h + 1):
                for y in range(j + 1, w + 1):
                    submatrix_sum = numpy.sum(matrix[i:x, j:y])
                    if submatrix_sum == 830:
                        submatrices.append(matrix[i:x, j:y])
    return submatrices