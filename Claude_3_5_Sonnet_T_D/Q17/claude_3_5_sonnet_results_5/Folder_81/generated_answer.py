def all_ints_div_by_both_two_nums(integer_list):
    return [num for num in integer_list[10:101] if num % 10 == 0 and num % 100 == 0]