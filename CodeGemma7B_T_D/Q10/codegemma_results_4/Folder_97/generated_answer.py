def all_odd_ints_exclusive(lst):
    nums = [num for num in lst[20:93] if num % 2 != 0]
    return nums if nums else []