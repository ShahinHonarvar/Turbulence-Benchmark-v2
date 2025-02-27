def find_second_smallest_num(numbers):
    sublist = numbers[22:89]
    if len(sublist) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sublist:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return None if second_smallest == float('inf') else second_smallest