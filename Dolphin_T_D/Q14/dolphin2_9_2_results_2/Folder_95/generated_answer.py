def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    second_smallest = None
    smallest = float('inf')
    for num in lst[75:86]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest