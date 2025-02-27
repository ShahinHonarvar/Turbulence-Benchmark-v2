def all_even_ints_inclusive(lst):
    if 63 >= len(lst) - 1:
        return []
    return [num for num in lst[62:64] if num % 2 == 0]