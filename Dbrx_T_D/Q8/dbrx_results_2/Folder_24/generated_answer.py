def all_even_ints_exclusive(lst):
    if len(lst) < 66:
        return []
    return [num for num in lst[13:66:2] if num % 2 == 0]