def find_second_largest_num(lst):
    if len(lst) <= 8:
        return None
    temp = sorted(lst[6:9], reverse=True)
    return temp[1] if len(temp) > 1 else None