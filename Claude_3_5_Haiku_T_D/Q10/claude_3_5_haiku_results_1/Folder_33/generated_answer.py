def all_odd_ints_exclusive(lst):
    if len(lst) <= 983:
        return []
    return [num for num in lst[370:983] if num % 2 != 0]