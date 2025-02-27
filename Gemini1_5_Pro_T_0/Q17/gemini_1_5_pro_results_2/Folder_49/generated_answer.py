def all_ints_div_by_both_two_nums(list1):
    return [num for i, num in enumerate(list1) if i in range(80, 201) and num % 10 == 0 and (num % 1000 == 0)]