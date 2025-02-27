def submatrix_with_n_numbers(matrix):
    """
    Count of all submatrices of the given matrix that contain 64 integers each.
    """
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(j + 1, len(matrix)):
                for l in range(k + 1, len(matrix)):
                    for m in range(l + 1, len(matrix)):
                        for n in range(m + 1, len(matrix)):
                            for o in range(n + 1, len(matrix)):
                                for p in range(o + 1, len(matrix)):
                                    for q in range(p + 1, len(matrix)):
                                        for r in range(q + 1, len(matrix)):
                                            for s in range(r + 1, len(matrix)):
                                                for t in range(s + 1, len(matrix)):
                                                    for u in range(t + 1, len(matrix)):
                                                        for v in range(u + 1, len(matrix)):
                                                            for w in range(v + 1, len(matrix)):
                                                                for x in range(w + 1, len(matrix)):
                                                                    for y in range(x + 1, len(matrix)):
                                                                        for z in range(y + 1, len(matrix)):
                                                                            for a in range(z + 1, len(matrix)):
                                                                                for b in range(a + 1, len(matrix)):
                                                                                    if len(set(matrix[i][j:a + 1][k][l:b + 1][m][n:o + 1][p][q:r + 1][s][t:u + 1][v][w:x + 1][x][y:z + 1])) == 64:
                                                                                        count += 1
    return count