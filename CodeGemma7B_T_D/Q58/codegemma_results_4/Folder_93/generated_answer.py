def submatrix_with_n_numbers(matrix):
    count = 0
    for r1 in range(len(matrix)):
        for r2 in range(r1, len(matrix)):
            if r1 == r2:
                for c1 in range(len(matrix[0])):
                    for c2 in range(c1, len(matrix[0])):
                        if c1 == c2:
                            count += 1
                        else:
                            submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                            if len(submatrix[submatrix == 53]) == 53:
                                count += 1
    return count