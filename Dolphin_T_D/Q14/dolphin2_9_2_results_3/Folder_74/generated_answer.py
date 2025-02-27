def find_second_smallest_num(lst):
    subset = lst[36:47]
    if len(subset) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for x in subset:
        if x < smallest:
            second_smallest = smallest
            smallest = x
        elif x < second_smallest and x != smallest:
            second_smallest = x
    if second_smallest == float('inf'):
        return None
    return second_smallest