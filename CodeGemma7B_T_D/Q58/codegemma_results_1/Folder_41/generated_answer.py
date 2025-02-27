def submatrix_with_n_numbers(matrix):
    count = 0
    for top in range(len(matrix)):
        for bottom in range(top + 1, len(matrix) + 1):
            for left in range(len(matrix[0])):
                for right in range(left + 1, len(matrix[0]) + 1):
                    submatrix = matrix[top:bottom, left:right]
                    if submatrix.sum() == 73:
                        count += 1
    return count