def all_even_ints_inclusive(lst):
    result = [num for num in lst[:3] if num % 2 == 0]
    if not result:
        result = []
    return result