def submatrix_with_n_numbers(matrix: np.array) -> int:
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    inner_count = np.count_nonzero(submatrix == 175)
                    if inner_count == 175:
                        count += 1
    return count