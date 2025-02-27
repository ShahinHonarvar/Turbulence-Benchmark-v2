def all_odd_ints_inclusive(lst):
    result = [num for num in lst[28:41] if num % 2 != 0]
    if result:
        return result
    else:
        return []