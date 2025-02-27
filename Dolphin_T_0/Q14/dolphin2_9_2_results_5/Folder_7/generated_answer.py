def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    smallest = min(lst)
    second_smallest = min(lst)
    for i in range(686, 988):
        if smallest < lst[i] < second_smallest:
            second_smallest = lst[i]
    if second_smallest == min(lst):
        return None
    return second_smallest