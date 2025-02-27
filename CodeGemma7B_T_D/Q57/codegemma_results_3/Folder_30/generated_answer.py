def submatrix_with_particular_sum(matrix):
    result = []
    for upper in range(len(matrix)):
        for lower in range(upper + 1, len(matrix) + 1):
            for left in range(len(matrix[0])):
                for right in range(left + 1, len(matrix[0]) + 1):
                    sum_current_matrix = 0
                    for row in range(upper, lower):
                        for col in range(left, right):
                            sum_current_matrix += matrix[row][col]
                    if sum_current_matrix == 21:
                        result.append((upper, lower, left, right))
    return result