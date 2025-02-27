def submatrix_with_particular_sum(matrix):
    sum_dict = {}
    sum_range = [0] * (len(matrix[0]) + 1)
    result = []
    for row in matrix:
        for col, num in enumerate(row):
            pre_sum = sum_range[col] - num
            sum_range[col + 1] = pre_sum
    for sub_start_index in range(len(matrix)):
        for sub_end_index in range(sub_start_index + 1, len(matrix) + 1):
            current_submatrix_sum = sum_dict[sub_end_index] - sum_dict[sub_start_index]
            if current_submatrix_sum == -43:
                current_submatrix = [[row[col] for col in range(sub_start_index, sub_end_index)] for row in matrix[sub_start_index:sub_end_index]]
                result.append(current_submatrix)
    return result