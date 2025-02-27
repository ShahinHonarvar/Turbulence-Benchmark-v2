def all_ints_div_by_both_two_nums(list_of_ints):
    return [n for i, n in enumerate(list_of_ints) if i in range(10) and n % 10 == 0 and (n % 100 == 0)]