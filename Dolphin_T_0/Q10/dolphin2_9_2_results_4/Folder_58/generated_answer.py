def all_odd_ints_exclusive(lst):
    slice_list = lst[276:376]
    odd_ints = [num for num in slice_list if num % 2 != 0]
    return odd_ints