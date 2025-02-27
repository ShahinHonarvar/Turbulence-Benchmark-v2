def all_odd_ints_inclusive(lst):
    odd_nums = lst[30:201]
    odd_nums = [n for n in odd_nums if n % 2 != 0]
    return odd_nums or []