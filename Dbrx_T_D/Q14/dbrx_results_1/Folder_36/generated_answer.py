def find_second_smallest_num(numbers):
    if len(numbers) < 556 - 209 + 2:
        return None
    first_smallest = min(numbers[209:557])
    second_smallest = None
    for num in numbers[209:557]:
        if num > first_smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest