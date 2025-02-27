import numpy as np

def submatrix_with_n_numbers(matrix):
    counts = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 41:
                for m in range(i, len(matrix)):
                    if m - i > 4:
                        break
                    for n in range(j, len(matrix[0])):
                        if n - j > 4:
                            break
                        if len(np.array(matrix[i:m + 1, j:n + 1])) == 25:
                            counts += 1
    return counts