def all_even_ints_inclusive(lst):
    if len(lst) <= 975:
        return []
    subset = lst[639:976]
    return [num for num in subset if num % 2 == 0]