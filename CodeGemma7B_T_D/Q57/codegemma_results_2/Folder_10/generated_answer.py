def submatrix_with_particular_sum(matrix):
    list_of_submatrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    sum_of_submatrix = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            sum_of_submatrix += matrix[m][n]
                    if sum_of_submatrix == 56:
                        list_of_submatrix.append([row[j:l + 1] for row in matrix[i:k + 1]])
    return list_of_submatrix