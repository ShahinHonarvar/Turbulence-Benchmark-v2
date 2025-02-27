def all_even_ints_exclusive(lst):
    result = [num for num in lst[743:867:2] if num % 2 == 0]
    return result