def submatrix_with_particular_sum(matrix):
    list_of_submatrices = []
    for top in range(len(matrix)):
        for bottom in range(top, len(matrix)):
            for left in range(len(matrix[0])):
                for right in range(left, len(matrix[0])):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if sum(submatrix.flatten()) == -15:
                        list_of_submatrices.append(list(submatrix))
    return list_of_submatrices