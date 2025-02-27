def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 31 or len(numbers) - 20 < 2:
        return None
    first_smallest = min(numbers[20:31])
    second_smallest = None
    for num in numbers[20:31]:
        if num > first_smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest