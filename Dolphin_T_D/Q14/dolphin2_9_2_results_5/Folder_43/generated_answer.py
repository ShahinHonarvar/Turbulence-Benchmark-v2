def find_second_smallest_num(lst):
    if len(lst[74:96]) < 2:
        return None
    else:
        return sorted(lst[74:96])[1]