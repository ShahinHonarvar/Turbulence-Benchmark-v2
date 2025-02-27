def find_second_smallest_num(lst):
    if 200 < len(lst) < 90:
        return None
    sub_lst = lst[90:201]
    if len(sub_lst) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sub_lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest