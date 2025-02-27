def find_second_smallest_num(lst):
    if len(lst) >= 9 and lst[4:9]:
        subset = sorted(lst[4:9])
        if subset[1]:
            return subset[1]
    return None