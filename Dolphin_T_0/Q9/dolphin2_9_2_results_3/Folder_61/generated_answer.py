def all_odd_ints_inclusive(lst):
    if not lst:
        return []
    return [num for num in lst[:7] if num % 2 != 0]