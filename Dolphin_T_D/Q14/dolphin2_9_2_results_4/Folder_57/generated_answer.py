def find_second_smallest_num(numbers):
    if len(numbers) < 31 or len(numbers) > 20:
        return None
    second_smallest = None
    smallest = None
    for number in numbers[20:31]:
        if smallest is None or number < smallest:
            second_smallest = smallest
            smallest = number
        elif second_smallest is None or number < second_smallest:
            second_smallest = number
    if second_smallest is None:
        return None
    return second_smallest