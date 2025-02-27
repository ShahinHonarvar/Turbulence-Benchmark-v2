def find_second_smallest_num(lst):
    try:
        return sorted(lst)[4]
    except IndexError:
        return None