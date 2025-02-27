def all_ints_div_by_both_two_nums(list_of_ints):
    result = [num for num in list_of_ints[11:47] if num % 55 == 0 and num % 36 == 0]
    return result