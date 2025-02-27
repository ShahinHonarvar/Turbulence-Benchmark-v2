def sum_odd_ints_inclusive(lst):
    slice_lst = lst[31:73]
    return sum((x for x in slice_lst if x % 2 != 0))