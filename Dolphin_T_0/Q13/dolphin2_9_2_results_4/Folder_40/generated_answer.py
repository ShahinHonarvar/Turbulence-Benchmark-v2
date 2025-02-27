def find_second_largest_num(lst):
    try:
        return sorted(lst[:3])[1]
    except IndexError:
        return None