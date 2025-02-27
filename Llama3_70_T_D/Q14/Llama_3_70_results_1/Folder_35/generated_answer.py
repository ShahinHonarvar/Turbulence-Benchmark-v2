def find_second_smallest_num(lst):
    if len(lst) > 39:
        temp = sorted(lst[15:40])
        if len(temp) > 1:
            return temp[1]
    return None