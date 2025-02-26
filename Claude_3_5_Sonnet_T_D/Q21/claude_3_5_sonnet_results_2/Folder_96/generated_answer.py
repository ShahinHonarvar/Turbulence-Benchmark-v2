def all_ints_div_by_num(integer_list):
    if len(integer_list) > 20:
        return [num for num in integer_list[20:21] if num % 2 == 0]
    else:
        return []