def find_second_smallest_num(numbers):
    if len(numbers) < 72:
        return None
    numbers = numbers[52:72]
    first_smallest, second_smallest = (None, None)
    for num in numbers:
        if first_smallest is None or num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest