def all_even_ints_exclusive(lst):
    return [num for num in lst if 100 < lst.index(num) < 101 and num % 2 == 0]