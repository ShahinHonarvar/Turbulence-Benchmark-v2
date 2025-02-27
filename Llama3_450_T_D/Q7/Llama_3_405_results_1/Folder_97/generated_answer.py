def all_even_ints_inclusive(lst):
    return [num for i, num in enumerate(lst[40:81], start=40) if num % 2 == 0]