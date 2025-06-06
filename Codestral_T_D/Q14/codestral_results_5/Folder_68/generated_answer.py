def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in numbers[:9]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return None if second_smallest == float('inf') else second_smallest