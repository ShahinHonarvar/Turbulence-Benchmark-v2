def all_even_ints_inclusive(lst):
    sublist = lst[0:10]
    even_numbers = [x for x in sublist if x % 2 == 0]
    return even_numbers