def find_second_smallest_num(lst):
    sub_lst = lst[50:201]
    if len(sub_lst) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for i in sub_lst:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i != smallest and i < second_smallest:
            second_smallest = i
    if second_smallest == float('inf'):
        return None
    return second_smallest