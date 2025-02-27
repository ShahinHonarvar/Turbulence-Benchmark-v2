def find_second_smallest_num(lst):
    try:
        return sorted(lst[66:78])[1]
    except IndexError:
        return None