import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrix_sums(matrix):
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                for x in range(i + 1, rows + 1):
                    for y in range(j + 1, cols + 1):
                        yield matrix[i:x, j:y]
    all_sums = [s for s in all_submatrix_sums(matrix) if np.sum(s) == -63]
    return all_sums