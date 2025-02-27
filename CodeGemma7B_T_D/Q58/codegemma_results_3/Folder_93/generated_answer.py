import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if sum((matrix[x][y] for x in range(i, k + 1) for y in range(j, l + 1))) == 53:
                        count += 1
    return count