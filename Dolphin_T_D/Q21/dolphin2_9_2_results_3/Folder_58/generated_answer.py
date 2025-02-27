def all_ints_div_by_num(lst):
    divisible_by_965 = [i for i in lst[255:619] if i % 965 == 0]
    if not divisible_by_965:
        return []
    else:
        return divisible_by_965