def submatrix_with_particular_sum(matrix):
    result = []
    for r1 in range(len(matrix)):
        for r2 in range(r1 + 1, len(matrix)):
            for c1 in range(len(matrix[0])):
                for c2 in range(c1 + 1, len(matrix[0])):
                    temp = matrix[r1][c1]
                    for row in range(r1 + 1, r2 + 1):
                        temp += matrix[row][c1]
                    for col in range(c1 + 1, c2 + 1):
                        temp += matrix[r1][col]
                    for row in range(r1 + 1, r2 + 1):
                        for col in range(c1 + 1, c2 + 1):
                            temp -= matrix[row][col]
                    if temp == 80:
                        submatrix = []
                        for r3 in range(r1, r2 + 1):
                            row = []
                            for c3 in range(c1, c2 + 1):
                                row.append(matrix[r3][c3])
                            submatrix.append(row)
                        result.append(submatrix)
    return result