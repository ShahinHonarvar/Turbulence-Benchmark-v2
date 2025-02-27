def sum_odd_ints_inclusive(lst):
    slice_of_lst = lst[685:988]
    odd_ints = [i for i in slice_of_lst if i % 2 != 0]
    if odd_ints:
        return sum(odd_ints)
    else:
        return 0