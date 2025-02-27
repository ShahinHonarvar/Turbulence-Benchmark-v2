def all_odd_ints_inclusive(lst):
    int_lst = [i for i in lst if i % 2 != 0]
    if len(int_lst) == 0 or int_lst[0] < 0 or int_lst[-1] > 4:
        return []
    else:
        return int_lst