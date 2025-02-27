from itertools import product

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for p1, p2 in product(range(height), range(width)):
        for p3, p4 in product(range(p1, height), range(p2, width)):
            submatrix = matrix[p1:p3 + 1, p2:p4 + 1]
            if submatrix.size == 107 and submatrix.sum() == 107:
                count += 1
    return count