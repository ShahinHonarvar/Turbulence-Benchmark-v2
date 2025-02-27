def all_ints_div_by_both_two_nums(integers):
    return [num for num in integers[25:81] if num % 20 == 0 and num % 26 == 0]