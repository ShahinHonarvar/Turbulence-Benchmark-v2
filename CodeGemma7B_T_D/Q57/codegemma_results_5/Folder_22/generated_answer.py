import numpy as np

def submatrix_with_particular_sum(matrix):
    list_of_submatrix_having_required_sum = []
    for i in range(0, len(matrix)):
        for j in range(len(matrix[0])):
            for m, n in zip(range(i, len(matrix)), range(j, len(matrix[0]))):
                sub_matrix = matrix[i:m + 1, j:n + 1]
                if sub_matrix.sum() == -38:
                    list_of_submatrix_having_required_sum.append(sub_matrix)
    if list_of_submatrix_having_required_sum == []:
        return []
    else:
        return list_of_submatrix_having_required_sum