from functools import cmp_to_key

def find_second_smallest_num(lst):
    try:
        lst.sort(key=cmp_to_key(lambda a, b: a - b))
        return lst[91:100][1]
    except (IndexError, ValueError):
        return None