def find_second_smallest_num(numbers):
    if len(numbers) < 12:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for i in range(10, 101):
        if i >= len(numbers):
            break
        if numbers[i] < smallest:
            second_smallest = smallest
            smallest = numbers[i]
        elif numbers[i] < second_smallest and numbers[i] != smallest:
            second_smallest = numbers[i]
    if second_smallest == float('inf'):
        return None
    return second_smallest