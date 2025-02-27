def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 5:
        return None
    first_smallest = min(numbers[0:5])
    second_smallest = None
    for num in numbers[0:5]:
        if num > first_smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest if second_smallest is not None else None