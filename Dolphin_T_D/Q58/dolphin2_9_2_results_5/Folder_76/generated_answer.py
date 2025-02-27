import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 159:
                for n in range(i, len(matrix)):
                    if np.all(matrix[n][j:j + 3] < 159) and np.sum(matrix[n][j:j + 3]) >= 159:
                        count += 1
                    else:
                        break
                    for m in range(j, len(matrix[0])):
                        if np.all(matrix[n][m:m + 3] < 159) and np.sum(matrix[n][m:m + 3]) >= 159:
                            count += 1
                        else:
                            break
    return count