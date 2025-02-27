def find_second_smallest_num(lst):
    temp = sorted(lst[56:58])
    if len(temp) < 2:
        return None
    return temp[1]