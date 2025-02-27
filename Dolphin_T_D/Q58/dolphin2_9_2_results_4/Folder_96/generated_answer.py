import numpy as np

def submatrix_with_n_numbers(matrix):
    length = len(matrix[0]) * len(matrix)
    list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in list:
                continue
            count = 1
            for x in range(i + 1, len(matrix)):
                if matrix[x][j] in list:
                    if count == 20:
                        return 1
                    else:
                        break
                else:
                    list.append(matrix[x][j])
                    count += 1
            if count == 20:
                return 1
    return 0