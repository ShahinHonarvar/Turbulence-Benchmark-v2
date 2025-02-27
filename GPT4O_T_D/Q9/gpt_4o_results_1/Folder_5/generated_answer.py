def all_odd_ints_inclusive(lst):
    if len(lst) < 10:
        return []
    return [num for num in lst[8:10] if num % 2 != 0]