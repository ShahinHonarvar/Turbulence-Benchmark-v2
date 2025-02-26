def sum_ints_div_by_either_nums(integers):
    valid_range = integers[18:53]
    result = sum((num for num in valid_range if num % 15 == 0 or num % 57 == 0))
    return result