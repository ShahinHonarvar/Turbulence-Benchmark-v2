import numpy as np

def submatrix_with_n_numbers(A):

    def is_submatrix(i, j, n):
        if j + n >= A.shape[1] or i + n >= A.shape[0]:
            return False
        return np.all(A[i:i + n, j:j + n] == 166)
    count = 0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            for n in range(1, A.shape[0] - i + 1):
                if is_submatrix(i, j, n):
                    count += 1
    return count