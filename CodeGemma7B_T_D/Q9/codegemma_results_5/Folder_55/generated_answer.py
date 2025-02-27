def all_odd_ints_inclusive(lst):
    if not any([num % 2 for num in lst[10:11]]):
        return []
    return [num for num in lst[10:11] if num % 2]