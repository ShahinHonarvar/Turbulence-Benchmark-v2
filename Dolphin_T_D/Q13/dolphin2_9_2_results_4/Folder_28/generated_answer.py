def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    try:
        second_largest = sorted(lst[62:64], reverse=True)[1]
    except IndexError:
        second_largest = None
    return second_largest