def all_odd_ints_inclusive(lst):
    result = [num for i, num in enumerate(lst[62:100]) if i >= 62 and i <= 99 and (num % 2 != 0)]
    return result if result else []