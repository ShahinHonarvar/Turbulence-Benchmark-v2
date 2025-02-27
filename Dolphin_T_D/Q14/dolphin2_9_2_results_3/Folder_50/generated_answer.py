def find_second_smallest_num(lst):
    values = lst[42:69]
    smallest = float('inf')
    second_smallest = float('inf')
    for num in values:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest