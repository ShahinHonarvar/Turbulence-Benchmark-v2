def all_ints_div_by_both_two_nums(input_list):
    if len(input_list) < 25:
        return []
    result = [num for num in input_list[22:25] if num % -85 == 0 and num % -30 == 0]
    return result