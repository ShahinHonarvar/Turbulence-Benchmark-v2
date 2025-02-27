import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n):
        for j in range(m):
            for x in range(i, n):
                for y in range(j, m):
                    sub_matrix = np.array(matrix[i:x + 1, j:y + 1])
                    if len(sub_matrix) == 5:
                        if len(sub_matrix[0]) == 7:
                            count += 1
    if count > 0:
        return count
    else:
        return 0