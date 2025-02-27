def all_ints_div_by_num(ints):
    return [num for idx, num in enumerate(ints) if idx >= 10 and idx <= 52 and (num % -12 == 0)]