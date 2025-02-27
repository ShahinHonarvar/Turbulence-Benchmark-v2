def find_second_largest_num(lst):
    try:
        return sorted(lst[21:98])[-2]
    except IndexError:
        return None