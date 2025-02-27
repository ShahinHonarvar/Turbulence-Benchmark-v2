import numpy

def submatrix_with_particular_sum(matrix):
    N = len(matrix)
    if N < 2:
        return []
    submatrices = []
    for i in range(N):
        for j in range(N):
            for k in range(i, N):
                for l in range(j, N):
                    submatrix_sum = numpy.sum(matrix[i:k + 1, j:l + 1])
                    if submatrix_sum == -82:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices