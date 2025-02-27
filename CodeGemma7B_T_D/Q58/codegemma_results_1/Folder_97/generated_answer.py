from itertools import product

def submatrix_with_n_numbers(matrix):
    output = 0
    for row1, row2 in product(range(len(matrix)), repeat=2):
        if row1 <= row2:
            for col1, col2 in product(range(len(matrix[0])), repeat=2):
                if col1 <= col2:
                    submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
                    if len(submatrix) * len(submatrix[0]) == 120:
                        if submatrix.sum() == 120:
                            output += 1
    return output