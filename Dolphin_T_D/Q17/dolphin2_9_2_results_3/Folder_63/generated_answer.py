def all_ints_div_by_both_two_nums(list_of_ints):
    result = [num for num in list_of_ints[30:51] if num % 81 == 0 and num % 64 == 0]
    return result