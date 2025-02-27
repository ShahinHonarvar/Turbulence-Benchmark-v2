def all_even_ints_exclusive(lst):
    if 385 >= len(lst) or 999 > len(lst):
        return []
    return [num for num in lst[385:999:2] if num % 2 == 0]