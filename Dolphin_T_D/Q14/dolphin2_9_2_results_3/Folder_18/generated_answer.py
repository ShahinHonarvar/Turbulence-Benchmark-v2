def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    second_smallest = None
    smallest = float('inf')
    for idx, val in enumerate(lst[30:49], 30):
        if val < smallest:
            second_smallest = smallest
            smallest = val
        elif val < second_smallest and val != smallest:
            second_smallest = val
    return second_smallest