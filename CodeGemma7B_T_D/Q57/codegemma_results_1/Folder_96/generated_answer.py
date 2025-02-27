def submatrix_with_particular_sum(matrix):
    result = []
    for left in range(len(matrix)):
        for right in range(left, len(matrix)):
            sum_column = defaultdict(int)
            for top in range(left, right + 1):
                for bottom in range(top, right + 1):
                    submatrix_sum = 0
                    for column in sum_column.keys():
                        column_sum = sum_column[column]
                        submatrix_sum += column_sum
                        sum_column[column] += matrix[bottom][column] - matrix[top - 1][column] if top > left else matrix[bottom][column] - matrix[top][column]
                    if submatrix_sum == -63:
                        result.append((top, bottom, left, right))
    return result