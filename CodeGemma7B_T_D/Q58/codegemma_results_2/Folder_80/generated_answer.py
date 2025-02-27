def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 180:
                for i in range(r, rows):
                    for j in range(c, cols):
                        submatrix = matrix[r:i + 1, c:j + 1]
                        if submatrix.shape[0] * submatrix.shape[1] == 180:
                            if submatrix.sum() == 180:
                                count += 1
    return count