def all_ints_div_by_num(input_list):
    if len(input_list) < 15:
        return []
    return [num for num in input_list[12:16] if num % -80 == 0]