def all_ints_div_by_both_two_nums(input_list):
    result = [num for num in input_list[78:82] if num % 76 == 0 and num % 60 == 0]
    return result