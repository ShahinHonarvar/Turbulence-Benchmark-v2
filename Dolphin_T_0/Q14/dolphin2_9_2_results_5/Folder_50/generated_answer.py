def find_second_smallest_num(lst):
    sublist = lst[42:69]
    try:
        return sorted(set(sublist))[1]
    except IndexError:
        return None