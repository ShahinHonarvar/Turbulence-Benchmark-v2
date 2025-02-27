def find_second_smallest_num(numbers):
    second_smallest = None
    smallest = float('inf')
    for num in numbers[36:47]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    if second_smallest is None:
        return None
    return second_smallest