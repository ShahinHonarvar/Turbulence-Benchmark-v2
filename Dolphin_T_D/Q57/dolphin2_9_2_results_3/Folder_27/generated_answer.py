import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    sums = np.cumsum(np.cumsum(matrix, 0), 1)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0] + 1):
                for l in range(j + 1, matrix.shape[1] + 1):
                    submatrix_sum = sums[k - 1, l - 1] - sums[i - 1, l - 1] - sums[k - 1, j - 1] + sums[i - 1, j - 1]
                    if submatrix_sum == 77:
                        result.append(matrix[i:k, j:l])
    return result