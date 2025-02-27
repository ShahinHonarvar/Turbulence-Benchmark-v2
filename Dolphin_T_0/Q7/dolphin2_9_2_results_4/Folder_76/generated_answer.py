def all_even_ints_inclusive(lst):
    if 686 <= 987 < len(lst):
        return [x for x in lst[686:988:2] if x % 2 == 0]
    else:
        return []