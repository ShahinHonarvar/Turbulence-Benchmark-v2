def all_even_ints_inclusive(lst):
    if len(lst) <= 975:
        return []
    return [num for num in lst[639:976] if num % 2 == 0]