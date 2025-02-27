from numpy import *

def submatrix_with_particular_sum(matrix):
    list_of_submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if sum(submatrix.flatten()) == 80:
                        list_of_submatrices.append(submatrix)
    if not list_of_submatrices:
        return []
    else:
        return list_of_submatrices