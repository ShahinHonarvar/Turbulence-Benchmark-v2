def find_second_smallest_num(lst):
    try:
        el1 = min(lst[56:58])
        lst.remove(el1)
        return min(lst[56:58])
    except ValueError:
        return None