def find_second_smallest_num(numbers):
    if len(numbers) < 27:
        return None
    first_smallest = min(numbers[56:83])
    second_smallest = None
    for num in numbers[56:83]:
        if num > first_smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest