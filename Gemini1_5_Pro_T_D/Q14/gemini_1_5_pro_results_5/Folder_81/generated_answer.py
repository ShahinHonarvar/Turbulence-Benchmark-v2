def find_second_smallest_num(numbers):
    if len(numbers) < 12:
        return None
    first_smallest = float('inf')
    second_smallest = float('inf')
    for i in range(10, 101):
        if i >= len(numbers):
            break
        if numbers[i] < first_smallest:
            second_smallest = first_smallest
            first_smallest = numbers[i]
        elif numbers[i] < second_smallest and numbers[i] != first_smallest:
            second_smallest = numbers[i]
    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest