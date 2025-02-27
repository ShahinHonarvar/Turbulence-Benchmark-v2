def submatrix_with_n_numbers(mat):
    count = 0
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            for r in range(row, len(mat)):
                for c in range(col, len(mat[r])):
                    if len(set((mat[i][j] for i in range(row, r + 1) for j in range(col, c + 1)))) == 17:
                        count += 1
    return count