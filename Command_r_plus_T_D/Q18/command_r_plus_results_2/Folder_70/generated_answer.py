def sum_ints_div_by_either_nums(lst):
    if 42 < len(lst) - 1:
        if lst[42] % 15 == 0 or lst[42] % 87 == 0:
            if lst[43] % 15 == 0 or lst[43] % 87 == 0:
                return lst[42] + lst[43]
            else:
                return lst[42]
        elif lst[43] % 15 == 0 or lst[43] % 87 == 0:
            return lst[43]
    return 0