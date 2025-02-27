def sum_odd_ints_inclusive(list):
    if not any((n % 2 for n in list[43:52])):
        return 0
    else:
        return sum((n for n in list[43:52] if n % 2))