def submatrix_with_particular_sum(matrix):
    submatrices = []
    for top in range(len(matrix)):
        for left in range(len(matrix[0])):
            for bottom in range(top, len(matrix)):
                for right in range(left, len(matrix[0])):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if submatrix.sum() == 21:
                        submatrices.append(submatrix)
    return submatrices