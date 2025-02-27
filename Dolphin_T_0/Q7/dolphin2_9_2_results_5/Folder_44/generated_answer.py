def all_even_ints_inclusive(lst):
    result = [num for num in lst[13:69] if num % 2 == 0]
    return result if result else []