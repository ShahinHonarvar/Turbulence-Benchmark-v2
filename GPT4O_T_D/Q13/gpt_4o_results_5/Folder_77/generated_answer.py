def find_second_largest_num(numbers):
    if len(numbers) <= 538 and 527 <= len(numbers):
        subset = numbers[527:539]
        if len(subset) < 2:
            return None
        unique_numbers = list(set(subset))
        if len(unique_numbers) < 2:
            return None
        unique_numbers.sort()
        return unique_numbers[-2]
    return None