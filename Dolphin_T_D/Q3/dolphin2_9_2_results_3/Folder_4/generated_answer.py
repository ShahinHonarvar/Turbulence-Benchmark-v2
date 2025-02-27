def all_pos_ints_inclusive(matrix):
    result = [num for num in matrix[12:93] if num > 0]
    return result if len(result) > 0 else []