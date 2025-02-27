def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if len(np.unique(submatrix)) == 104:
                        count += 1
    return count