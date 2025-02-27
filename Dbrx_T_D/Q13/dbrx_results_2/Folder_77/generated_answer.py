def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 538 or 527 > len(numbers) - 1:
        return None
    second_largest, largest = (None, None)
    for num in numbers[527:539]:
        if largest is None or num > largest:
            second_largest, largest = (largest, num)
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest