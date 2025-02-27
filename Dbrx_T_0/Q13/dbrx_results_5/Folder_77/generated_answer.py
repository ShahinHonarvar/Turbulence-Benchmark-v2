def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 538 or 527 > len(numbers) - 1:
        return None
    second_largest = None
    largest = max(numbers[527:539])
    for num in numbers[527:539]:
        if num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest