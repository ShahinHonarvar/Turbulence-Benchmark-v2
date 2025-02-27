def find_second_largest_num(lst):
    try:
        temp = sorted(set(lst[28:39]), reverse=True)
        return temp[1] if len(temp) > 1 else None
    except IndexError:
        return None