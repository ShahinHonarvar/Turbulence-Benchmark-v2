def all_ints_div_by_both_two_nums(int_list):
    if len(int_list) < 88:
        return []
    return [num for num in int_list[77:88] if num % 23 == 0 and num % 57 == 0]