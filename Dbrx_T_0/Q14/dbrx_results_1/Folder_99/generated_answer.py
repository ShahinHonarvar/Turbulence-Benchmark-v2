def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 608 or len(numbers) < 609:
        return None
    first_smallest = min(numbers[608:609])
    second_smallest = None
    for num in numbers[608:609]:
        if num > first_smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest