def all_odd_ints_inclusive(lst):
    if len(lst) <= 63:
        return []
    return [num for num in lst[62:64] if num % 2 != 0]