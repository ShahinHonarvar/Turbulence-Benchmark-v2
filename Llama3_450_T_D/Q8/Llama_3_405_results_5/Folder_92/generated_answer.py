def all_even_ints_exclusive(lst):
    if len(lst) < 2:
        return []
    return [num for num in lst[1:-1] if num % 2 == 0]