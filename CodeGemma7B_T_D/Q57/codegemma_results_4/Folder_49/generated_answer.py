import numpy as np

def submatrix_with_particular_sum(matrix):
    answer = []
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k, len(matrix[0])):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    matrix_sum = 0
                    for m in range(submatrix.shape[0]):
                        for n in range(submatrix.shape[1]):
                            matrix_sum += submatrix[m][n]
                    if matrix_sum == -42:
                        answer.append(submatrix)
    return answer