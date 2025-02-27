import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for r1 in range(rows):
        temp = np.zeros(cols, dtype=int)
        for r2 in range(r1, rows):
            temp += matrix[r2]
            sum_dict = {0: -1}
            cum_sum = 0
            for c in range(cols):
                cum_sum += temp[c]
                if cum_sum in sum_dict:
                    result.append(matrix[r1:r2 + 1, sum_dict[cum_sum] + 1:c + 1])
                if cum_sum not in sum_dict:
                    sum_dict[cum_sum] = c
    return result