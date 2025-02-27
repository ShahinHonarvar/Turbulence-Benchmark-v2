def submatrix_with_n_numbers(matrix):
    count = 0
    for top in range(len(matrix)):
        for left in range(len(matrix[0])):
            for bottom in range(top, len(matrix)):
                for right in range(left, len(matrix[0])):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if (submatrix == 103).sum() == 103:
                        count += 1
    return count