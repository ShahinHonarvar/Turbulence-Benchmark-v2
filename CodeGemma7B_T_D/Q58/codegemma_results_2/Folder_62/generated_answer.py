def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.where(matrix == 186, 1, 0).cumsum(axis=0).cumsum(axis=1) >= 186)