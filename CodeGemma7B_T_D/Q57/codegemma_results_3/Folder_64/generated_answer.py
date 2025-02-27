def submatrix_with_particular_sum(matrix):
    """
    Submatrix with particular sum func
    """
    result_list = []
    for top in range(len(matrix)):
        for left in range(len(matrix[0])):
            for bottom in range(top, len(matrix)):
                for right in range(left, len(matrix[0])):
                    area = matrix[bottom][right] - matrix[bottom][left - 1] - matrix[top - 1][right] + matrix[top - 1][left - 1]
                    if area == -4:
                        result_list.append([i for i in range(top, bottom + 1)])
                        result_list.append([j for j in range(left, right + 1)])
    return result_list