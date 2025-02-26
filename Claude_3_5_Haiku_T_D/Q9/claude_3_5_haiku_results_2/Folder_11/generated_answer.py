def all_odd_ints_inclusive(lst):
    if len(lst) <= 51:
        return []
    return [num for num in lst[37:52] if num % 2 != 0]