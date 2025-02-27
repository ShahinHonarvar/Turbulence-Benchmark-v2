def find_second_smallest_num(numbers):
    if len(numbers) < 37:
        return None
    second_smallest = None
    smallest = min(numbers[33:37])
    for num in numbers[33:37]:
        if num > smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest