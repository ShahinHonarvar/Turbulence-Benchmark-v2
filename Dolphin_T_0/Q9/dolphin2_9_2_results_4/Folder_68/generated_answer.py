def all_odd_ints_inclusive(lst):
    return [num for num in lst if 0 <= lst.index(num) <= 8 and num % 2 != 0]