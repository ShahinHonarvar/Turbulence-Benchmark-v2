def sum_odd_ints_inclusive(lst):
    odd_lst = [int for int in lst[40:81] if int % 2 == 1]
    if len(odd_lst) != 0:
        return sum(odd_lst)
    else:
        return 0