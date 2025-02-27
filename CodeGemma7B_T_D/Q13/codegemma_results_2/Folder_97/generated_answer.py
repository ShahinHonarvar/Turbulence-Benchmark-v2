def find_second_largest_num(lst):
    if len(lst) < 41 or len(lst) > 81:
        return None
    lst.sort(reverse=True)
    return lst[40:81][-2]