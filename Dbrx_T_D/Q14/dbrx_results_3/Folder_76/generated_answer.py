def find_second_smallest_num(numbers):
    if len(numbers) < 605 or len(numbers) < 536:
        return None
    first_smallest = min(numbers[:605])
    second_smallest = None
    for num in numbers[533:606]:
        if num > first_smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest