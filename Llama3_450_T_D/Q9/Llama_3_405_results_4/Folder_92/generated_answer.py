def all_odd_ints_inclusive(lst):
    if len(lst) < 2:
        if len(lst) == 1 and lst[0] % 2 != 0:
            return lst
        else:
            return []
    return [num for num in lst[:2] if num % 2 != 0]