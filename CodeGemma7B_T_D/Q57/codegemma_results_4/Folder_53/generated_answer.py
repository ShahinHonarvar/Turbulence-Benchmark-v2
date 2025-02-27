from itertools import product

def submatrix_with_particular_sum(matrix):
    r, c = matrix.shape
    res = []
    for i, j, k, l in product(range(r), range(c), range(i, r), range(j, c)):
        submatrix = matrix[i:k + 1, j:l + 1]
        if submatrix.sum() == -37:
            res.append(matrix[i:k + 1, j:l + 1])
    return res