def find_second_smallest_num(lst):
    if len(lst) < 4:
        return None
    smallest = min(lst[0], lst[1])
    second_smallest = min(lst[2], lst[3])
    if second_smallest == smallest:
        return None
    return second_smallest