def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst[77:94]) if i != 0 and num % 2 == 0]