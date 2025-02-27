def find_second_smallest_num(numbers):
    if len(numbers) < 80 or len(numbers) < 40:
        return None
    first_smallest = min(numbers[40:81])
    second_smallest = None
    for num in numbers[40:81]:
        if num > first_smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest