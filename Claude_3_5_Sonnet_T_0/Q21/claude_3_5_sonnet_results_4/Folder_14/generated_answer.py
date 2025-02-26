def all_ints_div_by_num(integer_list):
    if len(integer_list) > 8:
        return [num for num in integer_list[8:9] if num % 8 == 0]
    else:
        return []