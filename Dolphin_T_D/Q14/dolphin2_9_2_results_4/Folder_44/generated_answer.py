def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    smallest = second_smallest = float('inf')
    for i in range(91, 100):
        if lst[i] < smallest:
            second_smallest, smallest = (smallest, lst[i])
        elif lst[i] < second_smallest and lst[i] != smallest:
            second_smallest = lst[i]
    if second_smallest == float('inf'):
        return None
    return second_smallest