from itertools import product

def submatrix_with_particular_sum(matrix):
    result = []
    for row1, row2 in product(range(len(matrix)), repeat=2):
        for col1, col2 in product(range(len(matrix[0])), repeat=2):
            if row1 <= row2 and col1 <= col2:
                submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
                if submatrix.sum() == 2:
                    result.append(submatrix)
    return result