def all_odd_ints_exclusive(lst):
    lst = lst[14:76]
    result = [num for num in lst if num % 2 != 0]
    return result