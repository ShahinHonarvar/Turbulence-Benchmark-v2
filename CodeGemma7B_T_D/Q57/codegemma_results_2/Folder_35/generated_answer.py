from itertools import product

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i, j, k, l in product(range(len(matrix)), repeat=4):
        submatrix = matrix[i:k + 1, j:l + 1]
        if submatrix.sum() == 432:
            submatrices.append(submatrix)
    return submatrices