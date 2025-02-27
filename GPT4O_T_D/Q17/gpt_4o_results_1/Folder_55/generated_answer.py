def all_ints_div_by_both_two_nums(integers):
    return [num for num in integers[:10] if num % 10 == 0 and num % 100 == 0]