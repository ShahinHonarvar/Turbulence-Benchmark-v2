def find_second_smallest_num(num_list):
    if len(num_list) < 2:
        return None
    smallest = num_list[0]
    second_smallest = None
    for num in num_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or (num < second_smallest and num != smallest):
            second_smallest = num
    return second_smallest