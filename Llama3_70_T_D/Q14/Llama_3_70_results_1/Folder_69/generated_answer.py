def find_second_smallest_num(lst):
    temp = lst[25:88]
    if len(temp) < 2:
        return None
    temp.sort()
    return temp[1]