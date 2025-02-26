def all_odd_ints_inclusive(lst):
    if len(lst) <= 51:
        return []
    return [num for num in lst[43:52] if num % 2 != 0]