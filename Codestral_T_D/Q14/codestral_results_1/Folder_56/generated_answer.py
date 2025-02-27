def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in numbers:
        if num <= smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest