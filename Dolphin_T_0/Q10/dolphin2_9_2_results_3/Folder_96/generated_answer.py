def all_odd_ints_exclusive(lst):
    result = [num for i, num in enumerate(lst[50:200]) if num % 2 == 1]
    return result