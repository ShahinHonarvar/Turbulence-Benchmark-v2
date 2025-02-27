def submatrix_with_particular_sum(matrix):
    list1 = []
    for r in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for r1 in range(r, matrix.shape[0]):
                for j1 in range(j, matrix.shape[1]):
                    sum1 = 0
                    for i in range(r, r1 + 1):
                        for k in range(j, j1 + 1):
                            sum1 += matrix[i][k]
                    if sum1 == 616:
                        list1.append([[r, r1], [j, j1]])
    return list1