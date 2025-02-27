def find_second_smallest_num(lst):
    try:
        small = min(lst[28:33])
        lst.remove(small)
        return min(lst[28:33])
    except ValueError:
        return None