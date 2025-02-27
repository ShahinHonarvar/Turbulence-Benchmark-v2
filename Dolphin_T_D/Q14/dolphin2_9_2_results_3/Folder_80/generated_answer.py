def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for i in range(30, 88):
        if smallest > lst[i] > second_smallest:
            second_smallest = lst[i]
        elif lst[i] < smallest:
            second_smallest, smallest = (smallest, lst[i])
    if second_smallest == float('inf'):
        return None
    return second_smallest