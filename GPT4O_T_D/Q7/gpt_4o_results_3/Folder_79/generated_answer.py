def all_even_ints_inclusive(lst):
    if len(lst) < 5:
        return []
    return [num for num in lst[4:5] if num % 2 == 0]