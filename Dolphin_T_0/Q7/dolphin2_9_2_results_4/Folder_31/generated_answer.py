def all_even_ints_inclusive(lst):
    result = [num for num in lst[75:89] if num % 2 == 0]
    if result:
        return result
    else:
        return []