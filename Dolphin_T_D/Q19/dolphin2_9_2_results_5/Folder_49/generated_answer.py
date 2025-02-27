def all_ints_not_div_by_num(lst):
    return [num for num in lst[:80] + lst[200:] if num % 1000 != 0]