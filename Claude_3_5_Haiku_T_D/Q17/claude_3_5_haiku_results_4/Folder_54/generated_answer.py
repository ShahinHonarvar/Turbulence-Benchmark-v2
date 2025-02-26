def all_ints_div_by_both_two_nums(input_list):
    result = [num for num in input_list[13:92] if num % -65 == 0 and num % -62 == 0]
    return result