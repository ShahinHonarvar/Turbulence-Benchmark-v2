def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 24:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in num_list[23:24]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest