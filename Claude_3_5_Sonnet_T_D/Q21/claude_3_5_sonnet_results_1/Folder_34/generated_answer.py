def all_ints_div_by_num(integer_list):
    if len(integer_list) >= 31:
        return [num for num in integer_list[30:31] if num % 3 == 0]
    else:
        return []