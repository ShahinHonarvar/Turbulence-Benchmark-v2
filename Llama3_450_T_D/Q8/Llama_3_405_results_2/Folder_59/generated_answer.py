def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst[1:9]) if num % 2 == 0]