def find_second_smallest_num(num_list):
    if len(num_list) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in num_list[12:69]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None