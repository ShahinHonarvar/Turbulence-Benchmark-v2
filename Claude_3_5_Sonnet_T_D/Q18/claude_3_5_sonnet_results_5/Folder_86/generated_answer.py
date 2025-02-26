def sum_ints_div_by_either_nums(integer_list):
    if len(integer_list) < 80:
        return 0
    target_range = integer_list[54:80]
    sum_result = sum((num for num in target_range if num % 54 == 0 or num % 28 == 0))
    return sum_result