from numpy import *

def submatrix_with_particular_sum(mat):
    """
            This function takes a 2-dimensional numpy matrix as input and returns all submatrices with the sum of integers equal to -46.
            """
    submatrices = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            for k in range(i, len(mat)):
                for l in range(j, len(mat[0])):
                    submatrix = mat[i:k + 1, j:l + 1]
                    if sum(submatrix.flatten()) == -46:
                        submatrices.append(submatrix)
    return submatrices