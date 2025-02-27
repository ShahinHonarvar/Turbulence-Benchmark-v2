def all_odd_ints_inclusive(lst):
    if not lst:
        return []
    odd_nums = [num for num in lst[209:557] if num % 2 != 0]
    return odd_nums if odd_nums else []