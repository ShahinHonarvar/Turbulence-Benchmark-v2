def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(j, len(matrix)):
            for k in range(len(matrix)):
                for l in range(k, len(matrix)):
                    if set([matrix[x][y] for x in range(i, j + 1) for y in range(k, l + 1)]) == {179}:
                        count += 1
    return count