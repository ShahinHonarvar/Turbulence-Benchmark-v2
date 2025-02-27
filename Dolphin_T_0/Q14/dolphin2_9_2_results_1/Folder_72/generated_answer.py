def find_second_smallest_num(lst):
    sublist = [i for i in lst[82:87]]
    if len(sublist) < 2:
        return None
    else:
        return sorted(sublist)[1]