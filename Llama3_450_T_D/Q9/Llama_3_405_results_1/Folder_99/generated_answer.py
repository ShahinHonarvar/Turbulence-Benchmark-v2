def all_odd_ints_inclusive(lst):
    if len(lst) < 371:
        return [num for num in lst[310:] if num % 2 != 0]
    else:
        return [num for idx, num in enumerate(lst) if idx >= 310 and idx <= 370 and (num % 2 != 0)]