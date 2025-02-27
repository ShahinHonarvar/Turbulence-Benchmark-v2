from functools import reduce

def find_second_smallest_num(lst):
    try:
        return reduce(min, [x for x in lst[64:67] if x not in [min(lst)]])
    except:
        return None