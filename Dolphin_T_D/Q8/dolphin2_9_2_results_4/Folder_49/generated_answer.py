def all_even_ints_exclusive(lst):
    return [num for num in lst if 80 < lst.index(num) < 200 and num % 2 == 0]