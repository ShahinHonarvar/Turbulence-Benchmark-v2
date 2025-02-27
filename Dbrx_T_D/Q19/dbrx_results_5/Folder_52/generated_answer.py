def all_ints_not_div_by_num(input_list):
    if len(input_list) < 92 or len(input_list) < 50:
        return []
    return [num for num in input_list[50:92] if num % 16 != 0]