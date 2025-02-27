def all_even_ints_inclusive(lst):
    return [num for i, num in enumerate(lst[75:95], start=75) if num % 2 == 0]