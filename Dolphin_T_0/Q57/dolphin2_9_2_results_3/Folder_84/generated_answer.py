import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            m, n, k, l = (0, 0, float('inf'), float('inf'))
            while m <= i < m + k and n <= j < n + l:
                if (i - m + 1) * (j - n + 1) > k * l:
                    k, l = (i - m + 1, j - n + 1)
                if i + 1 - m + 1 <= k:
                    m = i + 1 - k + 1
                if j + 1 - n + 1 <= l:
                    n = j + 1 - l + 1
            submatrix = np.array(matrix[m:m + k, n:n + l])
            if submatrix.sum() == -308:
                submatrices.append(submatrix)
    return submatrices