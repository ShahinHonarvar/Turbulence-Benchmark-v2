def all_odd_ints_inclusive(lst):
    if not any((i % 2 != 0 and 32 <= i <= 35 for i in lst)):
        return []
    return [i for i in lst if i % 2 != 0 and 32 <= i <= 35]