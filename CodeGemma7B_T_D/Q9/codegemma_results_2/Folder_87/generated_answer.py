def all_odd_ints_inclusive(lst):
    if len(lst) < 36 or len(lst) > 46:
        return []
    return [num for num in lst[36:47] if num % 2 != 0]