def submatrix_with_particular_sum(matrix):
    sum_list = []
    for top in range(len(matrix)):
        for bottom in range(top + 1, len(matrix)):
            temp_sum = 0
            for left in range(len(matrix[top])):
                for right in range(left + 1, len(matrix[top])):
                    temp_sum += matrix[top][left] + matrix[top][right] + matrix[bottom][left] + matrix[bottom][right]
                    if temp_sum == -336:
                        sum_list.append(matrix[top][left:right + 1])
                        sum_list.append(matrix[top:bottom + 1][left])
                        sum_list.append(matrix[top:bottom + 1][right])
                        sum_list.append(matrix[top][left:right + 1])
    return sum_list