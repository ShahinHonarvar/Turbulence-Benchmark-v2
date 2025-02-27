import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    sub_matrix = np.array(matrix[i:k + 1, j:l + 1])
                    if sum(sub_matrix.flatten()) == -77:
                        result.append(sub_matrix)
    return result