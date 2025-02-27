def all_odd_ints_inclusive(lst):
    if 63 < len(lst):
        return [num for num in lst[62:64] if num % 2 != 0]
    return []