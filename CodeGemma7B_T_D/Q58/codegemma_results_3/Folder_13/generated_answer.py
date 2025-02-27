def submatrix_with_n_numbers(matrix):
    return len(np.argwhere(matrix.cumsum(axis=0) == 175))