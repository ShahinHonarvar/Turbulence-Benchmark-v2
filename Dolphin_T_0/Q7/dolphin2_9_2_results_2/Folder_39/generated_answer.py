def all_even_ints_inclusive(lst):
    result = [num for i, num in enumerate(lst[20:31]) if num % 2 == 0]
    return result