def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 33:
        return None
    second_largest = None
    largest = max(numbers[28:33])
    for num in numbers[28:33]:
        if num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest