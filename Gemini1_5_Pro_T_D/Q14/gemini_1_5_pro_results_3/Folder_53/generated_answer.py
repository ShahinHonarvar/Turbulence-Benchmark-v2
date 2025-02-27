def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 101:
        return None
    first_smallest = float('inf')
    second_smallest = float('inf')
    for i in range(1, min(len(numbers), 101)):
        if numbers[i] < first_smallest:
            second_smallest = first_smallest
            first_smallest = numbers[i]
        elif numbers[i] < second_smallest and numbers[i] != first_smallest:
            second_smallest = numbers[i]
    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest