def find_second_smallest_num(lst):
    try:
        lst[80:201].sort()
        return lst[81]
    except IndexError:
        return None