import numpy as np
import itertools

def submatrix_with_n_numbers(matrix):
    num_elements = 186
    num_rows, num_cols = matrix.shape
    all_submatrices = [combo for i in range(1, min(num_rows, num_cols) + 1) for combo in itertools.combinations(range(num_cols), i)]
    counter = 0
    for comb in all_submatrices:
        submatrix = matrix[:, comb]
        if np.count_nonzero(submatrix) == num_elements:
            counter += 1
    return counter