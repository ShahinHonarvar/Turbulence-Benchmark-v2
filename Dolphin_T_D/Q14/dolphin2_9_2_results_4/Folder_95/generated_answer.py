def find_second_smallest_num(lst):
    if len(lst) < 85:
        return None
    sublist = lst[74:86]
    if len(set(sublist)) < 2:
        return None
    second_smallest = sorted(sublist)[1]
    return second_smallest