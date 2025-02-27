def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 9:
        return None
    first_smallest = min(numbers[:9])
    second_smallest = None
    for num in numbers:
        if num > first_smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    if second_smallest is None or second_smallest == first_smallest:
        return None
    return second_smallest