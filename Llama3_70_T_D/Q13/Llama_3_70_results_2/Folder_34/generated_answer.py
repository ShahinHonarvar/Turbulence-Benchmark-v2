def find_second_largest_num(lst):
    temp = lst[16:62]
    temp = list(set(temp))
    temp.sort(reverse=True)
    if len(temp) < 2:
        return None
    return temp[1]