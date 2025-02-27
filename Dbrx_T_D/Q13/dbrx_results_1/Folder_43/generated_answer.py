def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 86 or len(numbers) - 68 < 2:
        return None
    first_largest = max(numbers[68:87])
    second_largest = None
    for num in numbers[68:87]:
        if num < first_largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest