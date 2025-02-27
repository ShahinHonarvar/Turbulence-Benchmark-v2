def composite_nums_between_indices(numbers):
    if len(numbers) < 538 or 527 > min(range(len(numbers))):
        return set()
    composite_numbers = {num for num in numbers[527:539] if num > 1 and any((num % d == 0 for d in range(2, num)))}
    return composite_numbers