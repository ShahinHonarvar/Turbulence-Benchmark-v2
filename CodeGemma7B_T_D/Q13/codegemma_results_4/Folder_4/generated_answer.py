def find_second_largest_num(lst):
    try:
        return sorted(lst[12:93], reverse=True)[1]
    except IndexError:
        return None