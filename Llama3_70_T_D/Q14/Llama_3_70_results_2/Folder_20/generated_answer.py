def find_second_smallest_num(lst):
    try:
        return sorted(lst[75:95])[1]
    except IndexError:
        return None