def submatrix_with_n_numbers(matrix):
    for rows in range(0, len(matrix)):
        for cols in range(0, len(matrix[0])):
            for r in range(rows, len(matrix)):
                for c in range(cols, len(matrix[0])):
                    if len(set((matrix[i][j] for i in range(rows, r + 1) for j in range(cols, c + 1)))) == 37:
                        return 1
    return 0