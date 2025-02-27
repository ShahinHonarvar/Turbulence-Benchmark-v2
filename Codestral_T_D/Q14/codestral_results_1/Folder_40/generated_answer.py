def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[0], numbers[1])
    second_smallest = max(numbers[0], numbers[1])
    for i in range(2, len(numbers)):
        if numbers[i] < smallest:
            second_smallest = smallest
            smallest = numbers[i]
        elif numbers[i] < second_smallest and numbers[i] != smallest:
            second_smallest = numbers[i]
    return second_smallest