def find_second_smallest_num(num_list):
    if not isinstance(num_list, list) or len(num_list) == 0:
        return None
    if len(num_list) <= 2:
        return None
    subset = num_list[10:66]
    if len(subset) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in subset:
        if num <= smallest:
            smallest = num
        if smallest < num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest