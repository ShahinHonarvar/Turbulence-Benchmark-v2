def all_odd_ints_inclusive(lst):
    if len(lst) <= 72:
        return []
    return [num for num in lst[31:73] if num % 2 != 0]