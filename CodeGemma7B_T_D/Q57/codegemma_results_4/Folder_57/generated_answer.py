def submatrix_with_particular_sum(matrix):
    output = []
    for r1 in range(len(matrix)):
        for r2 in range(r1, len(matrix)):
            for c1 in range(len(matrix[r1])):
                for c2 in range(c1, len(matrix[r1])):
                    if matrix[r1][c1:c2 + 1].sum() + matrix[r2][c1:c2 + 1].sum() - matrix[r2][c1:c1 + 1].sum() == 13:
                        output.append((r1, r2, c1, c2))
    return output