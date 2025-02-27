import numpy as np

def submatrix_with_n_numbers(A):
    N = len(A)
    M = len(A[0])
    return np.sum(np.all((A[:N - 18] != 0) & (A[N - 17:N] != 0), axis=1))