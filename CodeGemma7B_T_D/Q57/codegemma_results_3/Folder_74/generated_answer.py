from numpy import array

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for row1 in range(rows):
        for col1 in range(cols):
            for row2 in range(row1, rows):
                for col2 in range(col1, cols):
                    submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
                    if submatrix.sum() == 88:
                        submatrices.append(submatrix)
    return submatrices