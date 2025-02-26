def all_ints_not_div_by_num(input_list):
    if len(input_list) <= 37:
        return []
    result = [num for num in input_list[19:37] if num % -67 != 0]
    return result