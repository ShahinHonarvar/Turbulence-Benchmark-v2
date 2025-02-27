def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for i in range(5):
        if lst[i] < smallest:
            second_smallest = smallest
            smallest = lst[i]
        elif lst[i] < second_smallest:
            second_smallest = lst[i]
    if second_smallest == float('inf'):
        return None
    return second_smallest