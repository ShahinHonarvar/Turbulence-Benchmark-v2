def sum_in_range(lst):
    new_lst = [item for item in lst if item in range(142, 981, 1)]
    if not new_lst:
        return 0
    else:
        return sum(new_lst)