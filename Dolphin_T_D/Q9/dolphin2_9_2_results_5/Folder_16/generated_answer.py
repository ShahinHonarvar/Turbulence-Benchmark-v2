def all_odd_ints_inclusive(lst):
    range_lst = lst[33:37]
    odd_lst = [i for i in range_lst if i % 2 != 0]
    return odd_lst