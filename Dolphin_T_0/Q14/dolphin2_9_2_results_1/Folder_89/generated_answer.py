def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in lst[62:64]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest