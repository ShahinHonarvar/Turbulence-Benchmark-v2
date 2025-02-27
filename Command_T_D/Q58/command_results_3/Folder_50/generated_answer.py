import numpy as np

def submatrix_with_n_numbers(A):
    A = np.array(A)
    if not A.size:
        return 0
    cnt = 0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            cnt += np.sum(np.sum(A[i:i + 40, j:j + 40]) == 40)
    return cnt