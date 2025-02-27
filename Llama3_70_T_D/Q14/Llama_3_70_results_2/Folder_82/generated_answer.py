def find_second_smallest_num(lst):
    temp = sorted(lst[20:201])
    return temp[1] if len(temp) > 1 else None