def all_odd_ints_inclusive(lst):
    return [num for num in lst if num % 2 != 0 and lst.index(num) == 0]