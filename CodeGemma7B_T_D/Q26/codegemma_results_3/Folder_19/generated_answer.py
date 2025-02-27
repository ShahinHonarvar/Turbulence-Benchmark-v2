def sum_in_range(lst):
    new_lst = [i for i in lst if 7 <= i <= 8]
    return sum(new_lst) if new_lst else 0