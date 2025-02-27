def submatrix_with_particular_sum(matrix):
    """ finds all sub matrices in the matrix that adds upto already given value """
    list_of_submatrices = []
    sum_of_one_submatrix = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[k])):
                    list_of_submatrices.append(matrix[i:k + 1][j:l + 1])
    for matrix in list_of_submatrices:
        for row in matrix:
            sum_of_one_submatrix += sum(row)
        if sum_of_one_submatrix == -863:
            return list_of_submatrices
        else:
            sum_of_one_submatrix = 0
    return list_of_submatrices