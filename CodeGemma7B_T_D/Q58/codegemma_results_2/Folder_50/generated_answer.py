def submatrix_with_n_numbers(matrix):
    count = 0
    for r1 in range(len(matrix)):
        for r2 in range(r1 + 1, len(matrix)):
            for c1 in range(len(matrix[0])):
                for c2 in range(c1 + 1, len(matrix[0])):
                    count += matrix[r2][c2] - matrix[r1][c2] - matrix[r2][c1] + matrix[r1][c1] == 40
    return count