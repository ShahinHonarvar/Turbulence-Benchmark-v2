def find_second_smallest_num(numbers):
    if len(numbers) < 63 or len(numbers) > 2000 or (not all((isinstance(i, (int, float)) for i in numbers))):
        return None
    numbers = numbers[22:64]
    if len(numbers) < 2:
        return None
    first_smallest = min(numbers[:2])
    second_smallest = max(numbers[:2])
    for num in numbers[2:]:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif num < second_smallest and num != first_smallest:
            second_smallest = num
    if second_smallest == first_smallest:
        return None
    else:
        return second_smallest