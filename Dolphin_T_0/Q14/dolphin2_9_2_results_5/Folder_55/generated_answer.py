def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for num in lst[10:11]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return None if second_smallest == float('inf') else second_smallest