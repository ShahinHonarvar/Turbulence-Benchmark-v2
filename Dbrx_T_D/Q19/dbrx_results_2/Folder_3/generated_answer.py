def all_ints_not_div_by_num(input_list):
    start, end = (31, 69)
    result = [num for num in input_list[start:end] if num % -70 != 0]
    return result