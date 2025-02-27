def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    first_smallest = float('inf')
    second_smallest = float('inf')
    for i in range(7):
        if lst[i] < first_smallest:
            second_smallest = first_smallest
            first_smallest = lst[i]
        elif first_smallest < lst[i] < second_smallest:
            second_smallest = lst[i]
    if second_smallest == float('inf'):
        return None
    return second_smallest