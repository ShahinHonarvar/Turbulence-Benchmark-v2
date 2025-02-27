def find_second_largest_num(lst):
    if 59 >= len(lst):
        return None
    temp = lst[25:60]
    temp.sort(reverse=True)
    if len(temp) < 2:
        return None
    return temp[1]