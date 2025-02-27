import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = np.array(matrix[i:k + 1, j:l + 1].flatten())
                    if 147 in submatrix and len(submatrix) == 147:
                        count += 1
    return count