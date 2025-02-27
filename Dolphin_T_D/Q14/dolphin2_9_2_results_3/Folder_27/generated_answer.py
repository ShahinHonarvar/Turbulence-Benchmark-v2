def find_second_smallest_num(lst):
    if not lst:
        return None
    if len(lst) <= 2:
        return None
    second_smallest = None
    smallest = float('inf')
    for num in lst[25:60]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest