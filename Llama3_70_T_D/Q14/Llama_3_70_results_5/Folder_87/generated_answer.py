def find_second_smallest_num(lst):
    try:
        return sorted(lst[22:89])[1]
    except IndexError:
        return None