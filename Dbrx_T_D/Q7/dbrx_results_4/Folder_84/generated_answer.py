def all_even_ints_inclusive(lst):
    if len(lst) < 87:
        return []
    else:
        return [num for num in lst[43:87] if num % 2 == 0]