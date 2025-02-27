def all_odd_ints_exclusive(l):
    odd_nums = [num for num in l[42:87] if num % 2 != 0]
    return odd_nums if odd_nums else []