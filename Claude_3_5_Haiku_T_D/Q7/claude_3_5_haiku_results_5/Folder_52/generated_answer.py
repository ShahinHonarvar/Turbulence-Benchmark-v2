def all_even_ints_inclusive(lst):
    if len(lst) <= 38:
        return []
    range_subset = lst[28:39]
    return [num for num in range_subset if num % 2 == 0]