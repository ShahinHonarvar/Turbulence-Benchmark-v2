def all_odd_ints_exclusive(lst):
    ret_list = [num for index, num in enumerate(lst) if 25 < index < 80 and num % 2 != 0]
    return ret_list