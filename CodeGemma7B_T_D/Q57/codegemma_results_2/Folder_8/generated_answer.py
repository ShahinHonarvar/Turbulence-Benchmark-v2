import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_dict = {}
    cumulative_sum = np.cumsum(np.cumsum(matrix, axis=0), axis=1)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix_sum = cumulative_sum[k, l] - cumulative_sum[k, j - 1] - cumulative_sum[i - 1, l] + cumulative_sum[i - 1, j - 1]
                    if submatrix_sum == -61:
                        sum_dict[i, j, k, l] = cumulative_sum[k, l] - cumulative_sum[k, j - 1] - cumulative_sum[i - 1, l] + cumulative_sum[i - 1, j - 1]
    return list(sum_dict.values()) if sum_dict else []