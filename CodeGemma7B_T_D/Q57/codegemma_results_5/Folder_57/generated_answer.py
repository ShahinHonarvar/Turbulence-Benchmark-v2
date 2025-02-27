def submatrix_with_particular_sum(matrix):
    """submatrix_with_particular_sum: this function returns all submatrices with a sum of integers being 13"""
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 13:
                        submatrices.append(submatrix)
    return submatrices