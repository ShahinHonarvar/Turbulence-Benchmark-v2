def sum_odd_ints_inclusive(lst):
    odd_nums = sum([num for num in lst[17:79] if num % 2 != 0])
    return 0 if odd_nums == 0 else odd_nums