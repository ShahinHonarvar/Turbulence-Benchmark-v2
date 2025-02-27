def sum_even_ints_inclusive(lst):
    if not lst or not isinstance(lst[0], int) or (not 262 <= 746 < len(lst)):
        return 0
    else:
        return sum((x for x in lst[262:747] if x % 2 == 0))