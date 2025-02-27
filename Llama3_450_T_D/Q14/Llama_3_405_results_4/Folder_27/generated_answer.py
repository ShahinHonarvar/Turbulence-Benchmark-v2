def find_second_smallest_num(lst):
    try:
        return sorted(lst[25:60])[1]
    except IndexError:
        return None