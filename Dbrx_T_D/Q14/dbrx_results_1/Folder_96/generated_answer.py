def find_second_smallest_num(numbers):
    if len(numbers) < 51:
        return None
    first_smallest = min(numbers[49:200])
    second_smallest = None
    for num in numbers[49:200]:
        if num > first_smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    if second_smallest is not None:
        return second_smallest
    else:
        return None