def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for i in range(12, 93):
        if lst[i] < smallest:
            second_smallest = smallest
            smallest = lst[i]
        elif lst[i] < second_smallest and lst[i] != smallest:
            second_smallest = lst[i]
    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest