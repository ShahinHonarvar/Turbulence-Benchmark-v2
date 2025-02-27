def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return 'None'
    numbers = numbers[56:99]
    smallest = float('inf')
    second_smallest = float('inf')
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return 'None'
    return second_smallest