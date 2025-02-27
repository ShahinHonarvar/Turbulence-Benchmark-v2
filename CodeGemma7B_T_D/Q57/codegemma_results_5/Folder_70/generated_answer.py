def submatrix_with_particular_sum(matrix):
    lst = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    if sum((row[j:l + 1] for row in matrix[i:k + 1])) == 411:
                        lst.append([row[j:l + 1] for row in matrix[i:k + 1]])
    return lst