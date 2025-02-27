def find_second_smallest_num(lst):
    temp = lst[64:67]
    temp.sort()
    if len(temp) < 2:
        return None
    return temp[1]