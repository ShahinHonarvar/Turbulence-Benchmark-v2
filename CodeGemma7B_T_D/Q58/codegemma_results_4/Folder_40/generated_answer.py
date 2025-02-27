def submatrix_with_n_numbers(matrix):
    result = 0
    for r1 in range(len(matrix)):
        for r2 in range(r1 + 1, len(matrix) + 1):
            for c1 in range(len(matrix[0])):
                for c2 in range(c1 + 1, len(matrix[0]) + 1):
                    if sum((matrix[r][c] for r in range(r1, r2) for c in range(c1, c2))) == 1:
                        result += 1
    return result