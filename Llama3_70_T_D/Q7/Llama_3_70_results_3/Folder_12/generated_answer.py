def all_even_ints_inclusive(lst):
    return [num for idx, num in enumerate(lst[14:65], start=14) if num % 2 == 0]