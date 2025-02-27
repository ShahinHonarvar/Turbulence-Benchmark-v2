from itertools import dropwhile, takewhile

def all_ints_not_div_by_num(lst):
    return list(takewhile(lambda x: x % -68, dropwhile(lambda x: x % -68 == 0, lst[44:91])))