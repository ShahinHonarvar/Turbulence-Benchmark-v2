from itertools import product

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i, j in product(range(rows), range(cols)):
        for k in range(i + 1, rows):
            for l in range(j + 1, cols):
                submatrix = matrix[i:k + 1, j:l + 1]
                if submatrix.size == 19:
                    count += 1
    return count