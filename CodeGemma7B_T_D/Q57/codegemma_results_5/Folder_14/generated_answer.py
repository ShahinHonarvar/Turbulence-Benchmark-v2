def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k, len(matrix[0])):
                    sum_of_submatrix = sum((row[k:l + 1] for row in matrix[i:j + 1]))
                    if sum_of_submatrix == -93:
                        result.append([[row[k:l + 1] for row in submatrix[i:j + 1]] for submatrix in matrix])
    return result