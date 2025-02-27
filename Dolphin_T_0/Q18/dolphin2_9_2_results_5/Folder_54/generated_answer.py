def sum_ints_div_by_either_nums(lst):
    return sum((int for idx, int in enumerate(lst[12:92]) if int % -65 == 0 or int % -62 == 0))