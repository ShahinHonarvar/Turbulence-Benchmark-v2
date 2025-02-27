def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    try:
        second_largest = sorted(lst)[-2]
    except:
        return None
    if second_largest in range(64, 67):
        return second_largest
    else:
        return None