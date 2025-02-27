def find_second_largest_num(lst):
    if len(lst) < 80:
        return None
    temp = sorted(lst[29:80], reverse=True)
    if len(temp) < 2 or temp[0] == temp[1]:
        return None
    return temp[1]