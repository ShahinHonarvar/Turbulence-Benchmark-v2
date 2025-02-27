import numpy

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[k])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if numpy.array_equal(numpy.sort(submatrix.flatten()), numpy.arange(10, 20)):
                        count += 1
    return count