def all_odd_ints_inclusive(lst):
    return [num for num in lst[37:77:2] if num % 2 != 0 and 37 <= lst.index(num) <= 76]