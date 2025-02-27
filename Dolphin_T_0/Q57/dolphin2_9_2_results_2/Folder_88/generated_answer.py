import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_submatrix(subset, matrix):
        return all((all((x in y for x in subset)) for y in matrix))

    def get_sum(subset):
        return sum((x for x in subset))
    submatrices = []
    matrix_array = np.array(matrix).reshape(len(matrix), len(matrix[0]))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix) + 1):
                for l in range(j + 1, len(matrix[0]) + 1):
                    subset = matrix_array[i:k, j:l]
                    if is_submatrix(subset, matrix_array) and get_sum(subset) == -64:
                        submatrices.append(subset)
    return submatrices