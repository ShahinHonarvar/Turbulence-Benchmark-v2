def find_second_smallest_num(lst):
    sliced_lst = lst[30:201]
    if len(sliced_lst) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in sliced_lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest