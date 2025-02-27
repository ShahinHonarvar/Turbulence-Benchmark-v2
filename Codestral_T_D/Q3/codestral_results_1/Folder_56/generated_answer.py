def all_pos_ints_inclusive(lst):
    return [num for num in lst if num > 0 and lst.index(num) == 0]