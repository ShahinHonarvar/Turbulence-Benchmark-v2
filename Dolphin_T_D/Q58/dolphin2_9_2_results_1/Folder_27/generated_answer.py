import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 77
    shape = matrix.shape
    tuple_of_slices = tuple((slice(n, shape[0] - n, 1) for _ in range(shape[1] - n + 1)))
    count = 0
    for slice_1 in range(shape[0] - n + 1):
        for slice_2 in range(shape[1] - n + 1):
            submatrix = matrix[tuple_of_slices]
            if np.count_nonzero(submatrix == n):
                count += 1
    return count if count else 0