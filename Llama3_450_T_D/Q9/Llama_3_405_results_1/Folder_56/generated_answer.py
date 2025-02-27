def all_odd_ints_inclusive(lst):
    if not lst:
        return []
    return [num for num in lst[0:1] if num % 2 != 0]