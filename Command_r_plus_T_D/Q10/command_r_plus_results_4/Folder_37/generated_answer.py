def all_odd_ints_exclusive(lst):
    odd_ints = [i for i in lst[1:-1] if i % 2 != 0]
    return odd_ints