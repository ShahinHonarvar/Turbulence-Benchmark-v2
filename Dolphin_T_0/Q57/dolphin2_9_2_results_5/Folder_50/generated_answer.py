import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_of_parts = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for i1 in range(i, len(matrix)):
                for j1 in range(j, len(matrix[i])):
                    sum = np.sum(matrix[i:i1 + 1, j:j1 + 1])
                    if sum == 95:
                        sum_of_parts.append(matrix[i:i1 + 1, j:j1 + 1])
    return sum_of_parts