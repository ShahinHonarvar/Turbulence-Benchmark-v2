def submatrix_with_n_numbers(matrix):
    count = 0
    tot_rows = matrix.shape[0]
    tot_cols = matrix.shape[1]
    for r1 in range(tot_rows):
        for r2 in range(r1, tot_rows):
            for c1 in range(tot_cols):
                for c2 in range(c1, tot_cols):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if submatrix.size == 179:
                        count += 1
    return count