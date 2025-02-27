def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    from_index = max(0, 19)
    to_index = min(len(lst) - 1, 92)
    sub_lst = lst[from_index:to_index + 1]
    smallest = second_smallest = float('inf')
    for num in sub_lst:
        if num < smallest:
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest