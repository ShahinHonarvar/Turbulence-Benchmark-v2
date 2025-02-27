import numpy as np

def submatrix_with_n_numbers(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix)):
                for l in range(len(matrix[0])):
                    if i <= k and j <= l:
                        subarray = np.array(matrix[i:k + 1, j:l + 1])
                        if 107 in subarray and len(subarray) == 107:
                            sum += 1
    return sum