def find_second_smallest_num(lst):
    try:
        return sorted(lst[17:79])[1]
    except IndexError:
        return None