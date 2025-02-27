from itertools import islice

def all_pos_ints_exclusive(int_list):
    filtered_nums = (num for num in int_list if num > 0)
    return [num for num in islice(filtered_nums, 23, 45)]