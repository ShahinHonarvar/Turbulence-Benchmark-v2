import numpy

def submatrix_with_particular_sum(matrix):
    all_submatrices = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if numpy.sum(submatrix) == -59:
                        all_submatrices.append(submatrix)
    return all_submatrices