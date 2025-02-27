def all_odd_ints_inclusive(lst):
    start = 62
    end = 99
    return [a for a in lst[start:end + 1] if a % 2 != 0]