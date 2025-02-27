from itertools import product

def submatrix_with_particular_sum(matrix):
    """Function to find all submatrices of a given matrix
  with sum of elements equals to -93"""
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    sum = 0
                    for row in range(i, k + 1):
                        for col in range(j, l + 1):
                            sum += matrix[row][col]
                    if sum == -93:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices