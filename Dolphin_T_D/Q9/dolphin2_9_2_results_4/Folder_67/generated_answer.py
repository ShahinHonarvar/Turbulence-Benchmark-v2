def all_odd_ints_inclusive(lst):
    result = [num for num in lst[22:51] if num % 2 != 0]
    return result if len(result) > 0 else []