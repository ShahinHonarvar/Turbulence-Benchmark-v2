def all_even_ints_inclusive(lst):
    if len(lst) >= 46:
        return [num for num in lst[36:47] if num % 2 == 0]
    else:
        return []