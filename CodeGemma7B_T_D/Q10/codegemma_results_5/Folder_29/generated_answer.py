def all_odd_ints_exclusive(lst):
    odd_ints = [num for num in lst[48:76] if num % 2 != 0]
    return odd_ints if odd_ints else []