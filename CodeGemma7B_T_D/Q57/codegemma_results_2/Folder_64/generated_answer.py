import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_dict = {}
    submatrices = []
    for y1 in range(len(matrix)):
        for y2 in range(y1 + 1, len(matrix)):
            for x1 in range(len(matrix[0])):
                for x2 in range(x1 + 1, len(matrix[0])):
                    area = (y2 - y1 + 1) * (x2 - x1 + 1)
                    submatrix = matrix[y1:y2 + 1, x1:x2 + 1]
                    sum_matrix = np.sum(submatrix)
                    if sum_matrix in sum_dict:
                        if area == sum_dict[sum_matrix]:
                            submatrices.append(submatrix)
                    else:
                        sum_dict[sum_matrix] = area
    return submatrices