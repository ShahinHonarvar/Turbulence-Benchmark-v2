def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 2:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for num in num_list[20:201]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return None if second_smallest == float('inf') else second_smallest