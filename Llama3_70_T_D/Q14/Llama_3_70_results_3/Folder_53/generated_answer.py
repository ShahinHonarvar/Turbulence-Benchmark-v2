def find_second_smallest_num(num_list):
    second_smallest = None
    smallest = float('inf')
    for num in num_list[1:101]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest