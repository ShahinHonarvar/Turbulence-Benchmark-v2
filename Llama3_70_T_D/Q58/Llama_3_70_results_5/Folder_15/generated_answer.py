import numpy as np
import itertools

def submatrix_with_n_numbers(matrix):
    count = 0
    for size in range(1, matrix.shape[0] + 1):
        for indices in itertools.combinations(range(matrix.shape[0]), size):
            for col_size in range(1, matrix.shape[1] + 1):
                for col_indices in itertools.combinations(range(matrix.shape[1]), col_size):
                    submatrix = matrix[np.ix_(indices, col_indices)]
                    if submatrix.size == 2 and len(np.unique(submatrix)) == 2:
                        count += 1
    return count