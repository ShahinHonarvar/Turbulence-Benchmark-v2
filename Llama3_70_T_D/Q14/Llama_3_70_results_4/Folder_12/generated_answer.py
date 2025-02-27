def find_second_smallest_num(numbers):
    sliced_numbers = numbers[31:73]
    if len(sliced_numbers) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sliced_numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest